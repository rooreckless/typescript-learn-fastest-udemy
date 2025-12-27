"""
カテゴリ情報付き商品取得ユースケース
"""

from typing import Optional
from application.services.item_service import ItemService


class GetItemWithCategoriesUseCase:
    """カテゴリ情報付き商品取得ユースケース"""

    def __init__(self, item_service: ItemService):
        """
        Args:
            item_service: 商品サービス
        """
        self.item_service = item_service

    async def __call__(
        self,
        item_id: int
    ) -> Optional[dict]:
        """
        カテゴリ情報付きで商品を取得する
        
        Args:
            item_id: 商品ID
            
        Returns:
            商品情報とカテゴリリスト、存在しない場合はNone
        """
        # カテゴリ情報付きで商品を取得
        item_with_categories = await self.item_service.get_item_with_categories(item_id)
        
        return item_with_categories
