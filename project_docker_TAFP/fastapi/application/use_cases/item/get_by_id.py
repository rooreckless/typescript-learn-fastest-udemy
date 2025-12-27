"""
商品ID取得ユースケース
"""

from typing import Optional
from domain import ItemEntity
from application.services.item_service import ItemService


class GetItemByIdUseCase:
    """商品ID取得ユースケース"""

    def __init__(self, item_service: ItemService):
        """
        Args:
            item_service: 商品サービス
        """
        self.item_service = item_service

    async def __call__(
        self,
        item_id: int
    ) -> Optional[ItemEntity]:
        """
        IDで商品を取得する
        
        Args:
            item_id: 商品ID
            
        Returns:
            取得した商品エンティティ、存在しない場合はNone
        """
        # IDで商品を取得
        item = await self.item_service.get_item_by_id(item_id)
        
        return item
