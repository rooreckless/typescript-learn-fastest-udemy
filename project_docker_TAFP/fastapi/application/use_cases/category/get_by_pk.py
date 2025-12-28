"""
カテゴリ取得(pkで)ユースケース
"""

from domain import CategoryEntity
from application.services.category_service import CategoryService


class GetCategoryByPkUseCase:
    """カテゴリ取得(pkで)ユースケース"""

    def __init__(self, category_service: CategoryService):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service

    async def __call__(
        self,
        category_id: int
    ) -> CategoryEntity | None:
        """
        カテゴリを取得(pkで)する
        
        Args:
            category_id: カテゴリID
            
        Returns:
            取得したカテゴリ
        """


        # カテゴリを取得(pkで)
        category = await self.category_service.get_category_by_id(category_id)
        if not category:
            return None
        return category