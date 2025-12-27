"""
商品全取得ユースケース
"""

from typing import List
from domain import ItemEntity
from application.services.item_service import ItemService


class GetAllItemsUseCase:
    """商品全取得ユースケース"""

    def __init__(self, item_service: ItemService):
        """
        Args:
            item_service: 商品サービス
        """
        self.item_service = item_service

    async def __call__(
        self,
        skip: int = 0,
        limit: int = 100
    ) -> List[ItemEntity]:
        """
        商品をすべて取得する
        
        Args:
            skip: スキップする件数
            limit: 取得する最大件数
            
        Returns:
            取得した商品のリスト
        """
        # 商品をすべて取得
        items = await self.item_service.get_all_items(skip=skip, limit=limit)
        
        return items
