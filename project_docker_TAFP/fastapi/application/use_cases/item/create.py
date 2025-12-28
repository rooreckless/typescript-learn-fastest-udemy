"""
商品作成ユースケース
"""

from domain import ItemEntity
from application.services.item_service import ItemService
from domain.item import Name,Description,Price,CreatedBy,UpdatedBy
from presentation.schemas.items import ItemCreateRequest

class CreateItemUseCase:
    """商品作成ユースケース"""

    def __init__(self, item_service: ItemService):
        """
        Args:
            item_service: 商品サービス
        """
        self.item_service = item_service

    async def __call__(
        self,
        request: ItemCreateRequest,
    ) -> ItemEntity:
        """
        商品を作成する
        
        Args:
            request: 商品作成リクエスト
            
        Returns:
            作成された商品エンティティ
        """

        item = ItemEntity.create(
            name=Name.validate_value(request.name),
            description=Description.validate_value(request.description),
            price=Price.validate_value(request.price),
            created_by=CreatedBy.validate_value(request.created_by),
            updated_by=UpdatedBy.validate_value(request.created_by)
        )
        # 商品を作成
        created_item = await self.item_service.create_item(item)
        
        return created_item