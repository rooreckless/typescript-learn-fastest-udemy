"""
カテゴリ更新ユースケース
"""

from typing import Optional
from domain import CategoryEntity
from domain.category import Name,Description,UpdatedBy
from application.services.category_service import CategoryService
from presentation.schemas.categories import CategoryUpdateRequest

class UpdateCategoryUseCase:
    """カテゴリ更新ユースケース"""

    def __init__(self, category_service: CategoryService):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service

    async def __call__(
        self,
        request: CategoryUpdateRequest,
        category_id: int,
    ) -> CategoryEntity:
        """
        カテゴリを更新する
        
        Args:
            category_id: カテゴリID
            name: 新しいカテゴリ名（オプション）
            description: 新しいカテゴリ説明（オプション）
            updated_by: 更新者
            
        Returns:
            更新されたカテゴリエンティティ、存在しない場合はNone
        """
        # カテゴリを更新
        updated_category = await self.category_service.update_category(
            category_id=category_id,
            name=Name.validate_value(request.name),
            description=Description.validate_value(request.description),
            updated_by=UpdatedBy.validate_value(request.updated_by)
        )
        
        return updated_category
