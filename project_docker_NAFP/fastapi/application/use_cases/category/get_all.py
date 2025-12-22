"""
カテゴリ全取得ユースケース
"""

from domain import CategoryEntity
from application.category_service import CategoryService


class GetAllCategoriesUseCase:
    """カテゴリ全取得ユースケース"""

    def __init__(self, category_service: CategoryService):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service

    async def __call__(
        self,
        skip: int = 0,
        limit: int = 100
    ) -> CategoryEntity:
        """
        カテゴリをすべて取得する
        
        Args:
            skip: スキップする件数
            limit: 取得する最大件数
            
        Returns:
            取得したカテゴリのリスト
        """


        # カテゴリをすべて取得
        all_categories = await self.category_service.get_all_categories(skip=skip, limit=limit)
        
        return all_categories