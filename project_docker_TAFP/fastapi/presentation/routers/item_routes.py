"""
商品APIエンドポイント
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from infrastructure.database import provide_db
from presentation.dependencies import provide_item_service, require_admin
from ..schemas.common import (
    MessageResponse,
    
)
from ..schemas.items import (
    ItemCreateRequest,
    ItemUpdateRequest,
    ItemResponse
)
from ..schemas.item_category import ItemWithCategoriesResponse
from domain import UserEntity


router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.post(
    "",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="商品を作成"
)
async def create_item(
    request: ItemCreateRequest,
    db: AsyncSession = Depends(provide_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    新しい商品を作成します
    
    - **name**: 商品名
    - **description**: 商品説明
    - **price**: 価格（0以上）
    
    ※ 管理者権限が必要です
    """
    from application.use_cases.item.create import CreateItemUseCase
    service = provide_item_service(db)
    use_case = CreateItemUseCase(service)
    item = await use_case(
        request=request
    )
    return ItemResponse.model_validate(item)


@router.get(
    "",
    response_model=List[ItemResponse],
    summary="全商品を取得"
)
async def get_items(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(provide_db)
):
    """
    全商品のリストを取得します
    
    - **skip**: スキップする件数（デフォルト: 0）
    - **limit**: 取得する最大件数（デフォルト: 100）
    """
    from application.use_cases.item.get_all import GetAllItemsUseCase
    service = provide_item_service(db)
    use_case = GetAllItemsUseCase(service)
    items = await use_case(skip=skip, limit=limit)
    return [ItemResponse.model_validate(item) for item in items]


@router.get(
    "/{item_id}",
    response_model=ItemResponse,
    summary="商品をIDで取得"
)
async def get_item(
    item_id: int,
    db: AsyncSession = Depends(provide_db)
):
    """
    指定されたIDの商品を取得します
    
    - **item_id**: 商品ID
    """
    from application.use_cases.item.get_by_id import GetItemByIdUseCase
    service = provide_item_service(db)
    use_case = GetItemByIdUseCase(service)
    item = await use_case(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return ItemResponse.model_validate(item)


@router.get(
    "/{item_id}/with-categories",
    response_model=ItemWithCategoriesResponse,
    summary="カテゴリ情報付きで商品を取得"
)
async def get_item_with_categories(
    item_id: int,
    db: AsyncSession = Depends(provide_db)
):
    """
    指定されたIDの商品をカテゴリ情報付きで取得します
    
    - **item_id**: 商品ID
    """
    from application.use_cases.item.get_with_categories import GetItemWithCategoriesUseCase
    service = provide_item_service(db)
    use_case = GetItemWithCategoriesUseCase(service)
    item_with_categories = await use_case(item_id)
    if not item_with_categories:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return item_with_categories


@router.put(
    "/{item_id}",
    response_model=ItemResponse,
    summary="商品を更新"
)
async def update_item(
    item_id: int,
    request: ItemUpdateRequest,
    db: AsyncSession = Depends(provide_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    指定されたIDの商品情報を更新します
    
    - **item_id**: 商品ID
    - **name**: 新しい商品名（オプション）
    - **description**: 新しい商品説明（オプション）
    - **price**: 新しい価格（オプション）
    
    ※ 管理者権限が必要です
    """
    from application.use_cases.item.update import UpdateItemUseCase
    service = provide_item_service(db)
    use_case = UpdateItemUseCase(service)
    item = await use_case(
        item_id=item_id,
        request=request
    )
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return ItemResponse.model_validate(item)


@router.delete(
    "/{item_id}",
    response_model=MessageResponse,
    summary="商品を削除"
)
async def delete_item(
    item_id: int,
    db: AsyncSession = Depends(provide_db),
    admin_user: UserEntity = Depends(require_admin)
):
    """
    指定されたIDの商品を論理削除します
    
    - **item_id**: 商品ID
    
    ※ 管理者権限が必要です
    """
    from application.use_cases.item.delete import DeleteItemUseCase
    service = provide_item_service(db)
    use_case = DeleteItemUseCase(service)
    success = await use_case(item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return MessageResponse(message=f"Item {item_id} deleted successfully")
