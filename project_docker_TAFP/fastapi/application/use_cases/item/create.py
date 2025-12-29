"""
商品作成ユースケース
"""

from domain import ItemEntity, UserEntity
from application.services.item_service import ItemService
from domain.item import Name,Description,Price,CreatedBy,UpdatedBy
from presentation.schemas.items import ItemCreateRequest

class CreateItemUseCase:
    """商品作成ユースケース"""

    def __init__(self, item_service: ItemService, current_user: UserEntity):
        """
        Args:
            item_service: 商品サービス
            current_user: 現在のログインユーザー
        """
        self.item_service = item_service
        self.current_user = current_user

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
            created_by=CreatedBy.validate_value(self.current_user.name.value),
            updated_by=UpdatedBy.validate_value(self.current_user.name.value)
        )
        # 商品を作成
        created_item = await self.item_service.create_item(item)
        
        return created_item