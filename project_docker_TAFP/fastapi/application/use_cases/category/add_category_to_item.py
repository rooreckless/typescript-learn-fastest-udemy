"""
商品にカテゴリを追加するユースケース
"""

from application.services.category_service import CategoryService
from presentation.schemas.item_category import ItemCategoryRequest
from domain.item import CreatedBy
class AddCategoryToItemUseCase:
    """商品にカテゴリを追加するユースケース"""

    def __init__(self, category_service: CategoryService):
        """
        Args:
            category_service: カテゴリサービス
        """
        self.category_service = category_service

    async def __call__(
        self,
        request: ItemCategoryRequest
    ) -> None:
        """
        商品にカテゴリを追加する
        
        Args:
            item_id: 商品ID
            category_id: カテゴリID
            created_by: 作成者
        """
        # 商品にカテゴリを追加
        await self.category_service.add_category_to_item(
            item_id=request.item_id,
            category_id=request.category_id,
            created_by=CreatedBy.validate_value(request.created_by)
        )
