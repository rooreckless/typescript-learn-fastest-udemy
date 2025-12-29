"""
カテゴリ作成ユースケース
"""

from domain import CategoryEntity
from domain.category import Name,Description,CreatedBy,UpdatedBy
from application.services.category_service import CategoryService
from presentation.schemas.categories import CategoryCreateRequest
from domain.user import UserEntity

class CreateCategoryUseCase:
    """カテゴリ作成ユースケース"""

    def __init__(self, category_service: CategoryService,current_user: UserEntity):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service
        self.current_user = current_user
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
            name=Name.validate_value(request.name),
            description=Description.validate_value(request.description),
            created_by=CreatedBy.validate_value(self.current_user.name.value),
            updated_by=UpdatedBy.validate_value(self.current_user.name.value)
        )

        # カテゴリを永続化
        created_category = await self.category_service.create_category(category)
        
        # 作成されたカテゴリを返す
        return created_category
