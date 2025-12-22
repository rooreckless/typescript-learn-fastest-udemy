"""
カテゴリのpkを指定し、それに紐づく商品をすべて取得するユースケース
"""
from typing import List
from domain import ItemEntity
from application.category_service import CategoryService


class GetItemsByCategoryPkUseCase:
    """カテゴリのpkを指定し、それに紐づく商品をすべて取得するユースケース"""

    def __init__(self, category_service: CategoryService):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service

    async def __call__(
        self,
        category_id: int
    ) -> List[ItemEntity] | None:
        """
        カテゴリのpkを指定し、それに紐づく商品をすべて取得する
        
        Args:
            category_id: カテゴリID
            
        Returns:
            取得した商品のリストまたはNone
        """


        # カテゴリのpkを指定し、それに紐づく商品をすべて取得する
        items = await self.category_service.get_items_by_category(category_id)
        if not items:
            return None
        return items