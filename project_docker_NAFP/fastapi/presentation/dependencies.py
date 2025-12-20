"""
依存性注入（Dependency Injection）
FastAPIのDependsで使用するサービス・リポジトリのファクトリー関数
"""

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import get_db
from infrastructure.user_repository import UserRepository
from infrastructure.item_repository import ItemRepository
from infrastructure.category_repository import CategoryRepository
from infrastructure.item_category_repository import ItemCategoryRepository
from application.user_service import UserService
from application.item_service import ItemService
from application.category_service import CategoryService


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


def get_item_category_repository(db: AsyncSession) -> ItemCategoryRepository:
    """商品カテゴリ関連リポジトリを取得"""
    return ItemCategoryRepository(db)


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
    item_category_repo = get_item_category_repository(db)
    return ItemService(item_repo, item_category_repo)


def get_category_service(db: AsyncSession) -> CategoryService:
    """カテゴリサービスを取得"""
    category_repo = get_category_repository(db)
    item_category_repo = get_item_category_repository(db)
    return CategoryService(category_repo, item_category_repo)
