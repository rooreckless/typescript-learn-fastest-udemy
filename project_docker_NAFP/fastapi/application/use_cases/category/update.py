"""
カテゴリ更新ユースケース
"""

from typing import Optional
from domain import CategoryEntity
from application.services.category_service import CategoryService


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
        category_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        updated_by: Optional[str] = None
    ) -> Optional[CategoryEntity]:
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
            name=name,
            description=description,
            updated_by=updated_by
        )
        
        return updated_category
