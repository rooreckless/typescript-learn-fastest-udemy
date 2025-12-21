"""
商品カテゴリ関連リポジトリ実装
"""

from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from datetime import datetime

from domain import ItemEntity,CategoryEntity
from domain.repositories import AbstractItemCategoryRepository
from infrastructure.models import ItemModel, CategoryModel, ItemCategoryModel


class ItemCategoryRepository(AbstractItemCategoryRepository):
    """商品カテゴリ関連リポジトリ実装クラス"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_category_to_item(
        self, 
        item_id: int, 
        category_id: int, 
        created_by: str, 
        updated_by: str
    ) -> bool:
        """商品にカテゴリを追加"""
        # 既存の関連を確認
        result = await self.session.execute(
            select(ItemCategoryModel).where(
                and_(
                    ItemCategoryModel.item_id == item_id,
                    ItemCategoryModel.category_id == category_id
                )
            )
        )
        existing = result.scalar_one_or_none()
        
        if existing:
            # 論理削除されている場合は復元
            if existing.deleted_at:
                existing.deleted_at = None
                existing.updated_by = updated_by
                existing.updated_at = datetime.now()
                await self.session.flush()
                return True
            return True

        # 新規作成
        db_item_category = ItemCategoryModel(
            item_id=item_id,
            category_id=category_id,
            created_by=created_by,
            updated_by=updated_by,
        )
        self.session.add(db_item_category)
        await self.session.flush()
        await self.session.refresh(db_item_category)
        return True

    async def remove_category_from_item(self, item_id: int, category_id: int) -> bool:
        """商品からカテゴリを削除（論理削除）"""
        result = await self.session.execute(
            select(ItemCategoryModel).where(
                and_(
                    ItemCategoryModel.item_id == item_id,
                    ItemCategoryModel.category_id == category_id,
                    ItemCategoryModel.deleted_at.is_(None)
                )
            )
        )
        db_item_category = result.scalar_one_or_none()
        
        if not db_item_category:
            return False

        db_item_category.deleted_at = datetime.now()
        await self.session.flush()
        return True

    async def find_categories_by_item(self, item_id: int) -> List[CategoryEntity]:
        """商品に紐づくカテゴリを取得"""
        result = await self.session.execute(
            select(CategoryModel)
            .join(ItemCategoryModel, CategoryModel.id == ItemCategoryModel.category_id)
            .where(
                and_(
                    ItemCategoryModel.item_id == item_id,
                    ItemCategoryModel.deleted_at.is_(None),
                    CategoryModel.deleted_at.is_(None)
                )
            )
        )
        db_categories = result.scalars().all()
        return [CategoryEntity.model_validate(category) for category in db_categories]

    async def find_items_by_category(self, category_id: int) -> List[ItemEntity]:
        """カテゴリに紐づく商品を取得"""
        result = await self.session.execute(
            select(ItemModel)
            .join(ItemCategoryModel, ItemModel.id == ItemCategoryModel.item_id)
            .where(
                and_(
                    ItemCategoryModel.category_id == category_id,
                    ItemCategoryModel.deleted_at.is_(None),
                    ItemModel.deleted_at.is_(None)
                )
            )
        )
        db_items = result.scalars().all()
        return [ItemEntity.model_validate(item) for item in db_items]
