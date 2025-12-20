"""
カテゴリユースケース（アプリケーションサービス）
"""

from typing import List, Optional

from domain.entities import CategoryEntity, ItemCategoryEntity
from domain.repositories import ICategoryRepository, IItemCategoryRepository


class CategoryService:
    """カテゴリサービスクラス"""

    def __init__(
        self,
        category_repository: ICategoryRepository,
        item_category_repository: IItemCategoryRepository
    ):
        self.category_repository = category_repository
        self.item_category_repository = item_category_repository

    async def create_category(
        self,
        name: str,
        description: str,
        created_by: str
    ) -> CategoryEntity:
        """
        新しいカテゴリを作成
        
        Args:
            name: カテゴリ名
            description: カテゴリ説明
            created_by: 作成者
            
        Returns:
            作成されたカテゴリエンティティ
        """
        category = CategoryEntity(
            name=name,
            description=description,
            created_by=created_by,
            updated_by=created_by
        )
        return await self.category_repository.create(category)

    async def get_category_by_id(self, category_id: int) -> Optional[CategoryEntity]:
        """IDでカテゴリを取得"""
        return await self.category_repository.find_by_id(category_id)

    async def get_all_categories(self, skip: int = 0, limit: int = 100) -> List[CategoryEntity]:
        """全カテゴリを取得"""
        return await self.category_repository.find_all(skip, limit)

    async def update_category(
        self,
        category_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        updated_by: str = "system"
    ) -> Optional[CategoryEntity]:
        """
        カテゴリ情報を更新
        
        Args:
            category_id: カテゴリID
            name: 新しいカテゴリ名（オプション）
            description: 新しいカテゴリ説明（オプション）
            updated_by: 更新者
            
        Returns:
            更新されたカテゴリエンティティ
        """
        existing_category = await self.category_repository.find_by_id(category_id)
        if not existing_category:
            return None

        updated_category = CategoryEntity(
            id=category_id,
            name=name if name else existing_category.name,
            description=description if description else existing_category.description,
            created_by=existing_category.created_by,
            created_at=existing_category.created_at,
            updated_by=updated_by
        )

        return await self.category_repository.update(category_id, updated_category)

    async def delete_category(self, category_id: int) -> bool:
        """カテゴリを論理削除"""
        return await self.category_repository.delete(category_id)

    async def add_category_to_item(
        self,
        item_id: int,
        category_id: int,
        created_by: str
    ) -> ItemCategoryEntity:
        """
        商品にカテゴリを追加
        
        Args:
            item_id: 商品ID
            category_id: カテゴリID
            created_by: 作成者
            
        Returns:
            商品カテゴリ関連エンティティ
        """
        item_category = ItemCategoryEntity(
            item_id=item_id,
            category_id=category_id,
            created_by=created_by,
            updated_by=created_by
        )
        return await self.item_category_repository.add_category_to_item(item_category)

    async def remove_category_from_item(self, item_id: int, category_id: int) -> bool:
        """商品からカテゴリを削除"""
        return await self.item_category_repository.remove_category_from_item(item_id, category_id)

    async def get_categories_by_item(self, item_id: int) -> List[CategoryEntity]:
        """商品に紐づくカテゴリを取得"""
        return await self.item_category_repository.find_categories_by_item(item_id)
