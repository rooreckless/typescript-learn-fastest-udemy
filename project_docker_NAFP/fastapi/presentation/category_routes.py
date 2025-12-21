"""
カテゴリAPIエンドポイント
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from infrastructure.database import get_db
from presentation.dependencies import get_category_service, get_item_service, require_admin
from presentation.schemas import (
    CategoryCreateRequest,
    CategoryUpdateRequest,
    CategoryResponse,
    ItemCategoryRequest,
    ItemResponse,
    MessageResponse
)
from domain.entities import UserEntity


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post(
    "",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
    summary="カテゴリを作成"
)
async def create_category(
    request: CategoryCreateRequest,
    db: AsyncSession = Depends(get_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    新しいカテゴリを作成します
    
    - **name**: カテゴリ名
    - **description**: カテゴリ説明
    
    ※ 管理者権限が必要です
    """
    service = get_category_service(db)
    category = await service.create_category(
        name=request.name,
        description=request.description,
        created_by=request.created_by
    )
    return CategoryResponse.model_validate(category)


@router.get(
    "",
    response_model=List[CategoryResponse],
    summary="全カテゴリを取得"
)
async def get_categories(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """
    全カテゴリのリストを取得します
    
    - **skip**: スキップする件数（デフォルト: 0）
    - **limit**: 取得する最大件数（デフォルト: 100）
    """
    service = get_category_service(db)
    categories = await service.get_all_categories(skip=skip, limit=limit)
    return [CategoryResponse.model_validate(category) for category in categories]


@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
    summary="カテゴリをIDで取得"
)
async def get_category(
    category_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    指定されたIDのカテゴリを取得します
    
    - **category_id**: カテゴリID
    """
    service = get_category_service(db)
    category = await service.get_category_by_id(category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )
    return CategoryResponse.model_validate(category)


@router.get(
    "/{category_id}/items",
    response_model=List[ItemResponse],
    summary="カテゴリに紐づく商品を取得"
)
async def get_items_by_category(
    category_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    指定されたカテゴリに属する商品のリストを取得します
    
    - **category_id**: カテゴリID
    """
    item_service = get_item_service(db)
    items = await item_service.get_items_by_category(category_id)
    return [ItemResponse.model_validate(item) for item in items]


@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
    summary="カテゴリを更新"
)
async def update_category(
    category_id: int,
    request: CategoryUpdateRequest,
    db: AsyncSession = Depends(get_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    指定されたIDのカテゴリ情報を更新します
    
    - **category_id**: カテゴリID
    - **name**: 新しいカテゴリ名（オプション）
    - **description**: 新しいカテゴリ説明（オプション）
    
    ※ 管理者権限が必要です
    """
    service = get_category_service(db)
    category = await service.update_category(
        category_id=category_id,
        name=request.name,
        description=request.description,
        updated_by=request.updated_by
    )
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )
    return CategoryResponse.model_validate(category)


@router.delete(
    "/{category_id}",
    response_model=MessageResponse,
    summary="カテゴリを削除"
)
async def delete_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    指定されたIDのカテゴリを論理削除します
    
    - **category_id**: カテゴリID
    
    ※ 管理者権限が必要です
    """
    service = get_category_service(db)
    success = await service.delete_category(category_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )
    return MessageResponse(message=f"Category {category_id} deleted successfully")


@router.post(
    "/item-category",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED,
    summary="商品にカテゴリを追加"
)
async def add_category_to_item(
    request: ItemCategoryRequest,
    db: AsyncSession = Depends(get_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    商品にカテゴリを追加します
    
    - **item_id**: 商品ID
    - **category_id**: カテゴリID
    
    ※ 管理者権限が必要です
    """
    service = get_category_service(db)
    await service.add_category_to_item(
        item_id=request.item_id,
        category_id=request.category_id,
        created_by=request.created_by
    )
    return MessageResponse(
        message=f"Category {request.category_id} added to item {request.item_id}"
    )


@router.delete(
    "/item-category/{item_id}/{category_id}",
    response_model=MessageResponse,
    summary="商品からカテゴリを削除"
)
async def remove_category_from_item(
    item_id: int,
    category_id: int,
    db: AsyncSession = Depends(get_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    商品からカテゴリを削除します
    
    - **item_id**: 商品ID
    - **category_id**: カテゴリID
    
    ※ 管理者権限が必要です
    """
    service = get_category_service(db)
    success = await service.remove_category_from_item(item_id, category_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Relationship between item {item_id} and category {category_id} not found"
        )
    return MessageResponse(
        message=f"Category {category_id} removed from item {item_id}"
    )
