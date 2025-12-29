"""
カテゴリリポジトリ実装
"""

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from datetime import datetime,timezone,timedelta
from domain import CategoryEntity,AbstractCategoryRepository, ItemEntity
from .model import CategoryModel
from ..item_category import ItemCategoryModel
from ..item import ItemModel

jst = timezone(timedelta(hours=+9), 'JST')

class CategoryRepository(AbstractCategoryRepository):
    """カテゴリリポジトリ実装クラス"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, category: CategoryEntity) -> CategoryEntity:
        """カテゴリを作成"""
        db_category = CategoryModel(
            name=category.name.value,
            description=category.description.value,
            created_by=category.created_by.value,
            created_at=datetime.now(tz=jst),
            updated_by=category.updated_by.value,
            updated_at=datetime.now(tz=jst)
        )
        self.session.add(db_category)
        await self.session.flush()
        # await self.session.refresh(db_category)
        await self.session.commit()
        return CategoryEntity.model_validate(db_category, from_attributes=True)

    async def find_by_id(self, category_id: int) -> Optional[CategoryEntity]:
        """IDでカテゴリを検索"""
        result = await self.session.execute(
            select(CategoryModel).where(
                CategoryModel.id == category_id,
                CategoryModel.deleted_at.is_(None)
            )
        )
        db_category = result.scalar_one_or_none()
        return CategoryEntity.model_validate(db_category, from_attributes=True) if db_category else None

    async def find_all(self, skip: int = 0, limit: int = 100) -> List[CategoryEntity]:
        """全カテゴリを取得"""
        result = await self.session.execute(
            select(CategoryModel)
            .where(CategoryModel.deleted_at.is_(None))
            .offset(skip)
            .limit(limit)
        )
        db_categories = result.scalars().all()
        return [CategoryEntity.model_validate(category, from_attributes=True) for category in db_categories]

    async def update(self, category_id: int, category: CategoryEntity) -> Optional[CategoryEntity]:
        """カテゴリを更新"""
        result = await self.session.execute(
            select(CategoryModel).where(
                CategoryModel.id == category_id,
                CategoryModel.deleted_at.is_(None)
            )
        )
        db_category = result.scalar_one_or_none()
        
        if not db_category:
            return None

        db_category.name = category.name.value
        db_category.description = category.description.value
        db_category.updated_by = category.updated_by.value
        db_category.updated_at = datetime.now(tz=jst)

        await self.session.flush()
        # await self.session.refresh(db_category)
        await self.session.commit()
        return CategoryEntity.model_validate(db_category, from_attributes=True)

    async def delete(self, category_id: int) -> bool:
        """カテゴリを論理削除"""
        result = await self.session.execute(
            select(CategoryModel).where(
                CategoryModel.id == category_id,
                CategoryModel.deleted_at.is_(None)
            )
        )
        db_category = result.scalar_one_or_none()
        
        if not db_category:
            return False
        db_category.updated_at = datetime.now(tz=jst)
        db_category.deleted_at = datetime.now(tz=jst)
        await self.session.flush()
        await self.session.commit()
        return True

    # 以下、旧ItemCategoryRepositoryから移動したメソッド
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
