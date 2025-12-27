"""
カテゴリ削除ユースケース
"""

from application.services.category_service import CategoryService


class DeleteCategoryUseCase:
    """カテゴリ削除ユースケース"""

    def __init__(self, category_service: CategoryService):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service

    async def __call__(
        self,
        category_id: int
    ) -> bool:
        """
        カテゴリを論理削除する
        
        Args:
            category_id: カテゴリID
            
        Returns:
            削除が成功した場合True、失敗した場合False
        """
        # カテゴリを削除
        success = await self.category_service.delete_category(category_id)
        
        return success
