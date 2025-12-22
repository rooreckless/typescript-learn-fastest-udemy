"""
ユーザーAPIエンドポイント
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from infrastructure.database import provide_db
from presentation.dependencies import provide_user_service, require_admin
from ..schemas.users import (
    UserCreateRequest,
    UserUpdateRequest,
    UserResponse
)
from ..schemas.common import MessageResponse
from domain import UserEntity


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="ユーザーを作成"
)
async def create_user(
    request: UserCreateRequest,
    db: AsyncSession = Depends(provide_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    新しいユーザーを作成します
    
    - **name**: ユーザー名
    - **email**: メールアドレス（一意）
    - **password**: パスワード（8文字以上）
    
    ※ 管理者権限が必要です
    """
    service = provide_user_service(db)
    try:
        user = await service.create_user(
            name=request.name,
            email=request.email,
            password=request.password,
            admin=request.admin,
            created_by=request.created_by
        )
        return UserResponse.model_validate(user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
    "",
    response_model=List[UserResponse],
    summary="全ユーザーを取得"
)
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(provide_db)
):
    """
    全ユーザーのリストを取得します
    
    - **skip**: スキップする件数（デフォルト: 0）
    - **limit**: 取得する最大件数（デフォルト: 100）
    """
    service = provide_user_service(db)
    users = await service.get_all_users(skip=skip, limit=limit)
    return [UserResponse.model_validate(user) for user in users]


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="ユーザーをIDで取得"
)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(provide_db)
):
    """
    指定されたIDのユーザーを取得します
    
    - **user_id**: ユーザーID
    """
    service = provide_user_service(db)
    user = await service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return UserResponse.model_validate(user)


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    summary="ユーザーを更新"
)
async def update_user(
    user_id: int,
    request: UserUpdateRequest,
    db: AsyncSession = Depends(provide_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    指定されたIDのユーザー情報を更新します
    
    - **user_id**: ユーザーID
    - **name**: 新しいユーザー名（オプション）
    - **email**: 新しいメールアドレス（オプション）
    - **password**: 新しいパスワード（オプション）
    
    ※ 管理者権限が必要です
    """
    service = provide_user_service(db)
    try:
        user = await service.update_user(
            user_id=user_id,
            name=request.name,
            email=request.email,
            password=request.password,
            admin=request.admin,
            updated_by=request.updated_by
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        return UserResponse.model_validate(user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete(
    "/{user_id}",
    response_model=MessageResponse,
    summary="ユーザーを削除"
)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(provide_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    指定されたIDのユーザーを論理削除します
    
    - **user_id**: ユーザーID
    
    ※ 管理者権限が必要です
    """
    service = provide_user_service(db)
    success = await service.delete_user(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return MessageResponse(message=f"User {user_id} deleted successfully")
    return MessageResponse(message=f"User {user_id} deleted successfully")
