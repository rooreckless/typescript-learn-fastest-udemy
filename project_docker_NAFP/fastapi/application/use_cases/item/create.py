"""
商品作成ユースケース
"""

from domain import ItemEntity
from application.services.item_service import ItemService


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
        name: str,
        description: str,
        price: float,
        created_by: str
    ) -> ItemEntity:
        """
        商品を作成する
        
        Args:
            name: 商品名
            description: 商品説明
            price: 価格
            created_by: 作成者
            
        Returns:
            作成された商品エンティティ
        """
        # 商品を作成
        item = await self.item_service.create_item(
            name=name,
            description=description,
            price=price,
            created_by=created_by
        )
        
        return item
