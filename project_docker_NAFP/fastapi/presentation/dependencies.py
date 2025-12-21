"""
依存性注入（Dependency Injection）
FastAPIのDependsで使用するサービス・リポジトリのファクトリー関数
"""

from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import get_db
from infrastructure.user.repository import UserRepository
from infrastructure.item.repository import ItemRepository
from infrastructure.category.repository import CategoryRepository
from application.user_service import UserService
from application.item_service import ItemService
from application.category_service import CategoryService
from domain import UserEntity
from presentation.auth import decode_access_token


# HTTPベアラートークン認証
security = HTTPBearer()


# =========================================
# リポジトリファクトリー
# =========================================

def get_user_repository(db: AsyncSession) -> UserRepository:
    """ユーザーリポジトリを取得"""
    return UserRepository(db)


def get_item_repository(db: AsyncSession) -> ItemRepository:
    """商品リポジトリを取得"""
    return ItemRepository(db)


def get_category_repository(db: AsyncSession) -> CategoryRepository:
    """カテゴリリポジトリを取得"""
    return CategoryRepository(db)


# =========================================
# サービスファクトリー
# =========================================

def get_user_service(db: AsyncSession) -> UserService:
    """ユーザーサービスを取得"""
    user_repo = get_user_repository(db)
    return UserService(user_repo)


def get_item_service(db: AsyncSession) -> ItemService:
    """商品サービスを取得"""
    item_repo = get_item_repository(db)
    return ItemService(item_repo)


def get_category_service(db: AsyncSession) -> CategoryService:
    """カテゴリサービスを取得"""
    category_repo = get_category_repository(db)
    item_repo = get_item_repository(db)
    return CategoryService(category_repo, item_repo)


# =========================================
# 認証・認可
# =========================================

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> UserEntity:
    """
    現在のユーザーを取得
    JWTトークンからユーザー情報を取得し、そのユーザー情報を返す
    """
    # トークンをデコード
    payload = decode_access_token(credentials.credentials)
    
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # ペイロードからユーザーIDを取得
    user_id: str = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # ユーザー情報を取得
    user_service = get_user_service(db)
    user = await user_service.get_user_by_id(int(user_id))
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user


async def require_admin(
    current_user: UserEntity = Depends(get_current_user)
) -> UserEntity:
    """
    管理者権限を要求
    現在のユーザーが管理者でない場合は403エラーを返す
    """
    if not current_user.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    
    return current_user

