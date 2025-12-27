"""
商品からカテゴリを削除するユースケース
"""

from application.services.category_service import CategoryService


class RemoveCategoryFromItemUseCase:
    """商品からカテゴリを削除するユースケース"""

    def __init__(self, category_service: CategoryService):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service

    async def __call__(
        self,
        item_id: int,
        category_id: int
    ) -> bool:
        """
        商品からカテゴリを削除する
        
        Args:
            item_id: 商品ID
            category_id: カテゴリID
            
        Returns:
            削除が成功した場合True、失敗した場合False
        """
        # 商品からカテゴリを削除
        success = await self.category_service.remove_category_from_item(
            item_id=item_id,
            category_id=category_id
        )
        
        return success
