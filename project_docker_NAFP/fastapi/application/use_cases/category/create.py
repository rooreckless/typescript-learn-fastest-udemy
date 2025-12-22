"""
カテゴリ作成ユースケース
"""

from domain import CategoryEntity
from application.category_service import CategoryService
from presentation.schemas.categories import CategoryCreateRequest


class CreateCategoryUseCase:
    """カテゴリ作成ユースケース"""

    def __init__(self, category_service: CategoryService):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service

    async def __call__(
        self,
        request: CategoryCreateRequest
    ) -> CategoryEntity:
        """
        カテゴリを作成する
        
        Args:
            request: カテゴリ作成リクエスト
            
        Returns:
            作成されたカテゴリのレスポンス
        """
        # カテゴリエンティティを作成
        category = CategoryEntity.create(
            name=request.name,
            description=request.description,
            created_by=request.created_by,
            updated_by=request.created_by
        )

        # カテゴリを永続化
        created_category = await self.category_service.create_category(category)
        
        # レスポンスに変換して返す
        return created_category
