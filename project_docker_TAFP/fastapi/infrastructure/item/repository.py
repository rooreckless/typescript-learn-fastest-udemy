"""
商品リポジトリ実装
"""

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from datetime import datetime,timezone,timedelta

from domain.item import ItemEntity,AbstractItemRepository
from domain import CategoryEntity
from .model import ItemModel
from ..category import CategoryModel
from ..item_category import ItemCategoryModel

jst = timezone(timedelta(hours=+9), 'JST')

class ItemRepository(AbstractItemRepository):
    """商品リポジトリ実装クラス"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, item: ItemEntity) -> ItemEntity:
        """商品を作成"""
        db_item = ItemModel(
            name=item.name.value,
            description=item.description.value,
            price=item.price.value,
            created_by=item.created_by.value,
            created_at=datetime.now(tz=jst),
            updated_by=item.updated_by.value,
            updated_at=datetime.now(tz=jst)
        )
        self.session.add(db_item)
        await self.session.flush()
        # await self.session.refresh(db_item)
        await self.session.commit()
        return ItemEntity.model_validate(db_item)

    async def find_by_id(self, item_id: int) -> Optional[ItemEntity]:
        """IDで商品を検索"""
        result = await self.session.execute(
            select(ItemModel).where(
                ItemModel.id == item_id,
                ItemModel.deleted_at.is_(None)
            )
        )
        db_item = result.scalar_one_or_none()
        return ItemEntity.model_validate(db_item) if db_item else None

    async def find_all(self, skip: int = 0, limit: int = 100) -> List[ItemEntity]:
        """全商品を取得"""
        result = await self.session.execute(
            select(ItemModel)
            .where(ItemModel.deleted_at.is_(None))
            .offset(skip)
            .limit(limit)
        )
        db_items = result.scalars().all()
        return [ItemEntity.model_validate(item) for item in db_items]

    async def update(self, item: ItemEntity) -> Optional[ItemEntity]:
        """商品を更新"""
        result = await self.session.execute(
            select(ItemModel).where(
                ItemModel.id == item.id,
                ItemModel.deleted_at.is_(None)
            )
        )
        db_item = result.scalar_one_or_none()
        
        if not db_item:
            return None

        db_item.name = item.name.value
        db_item.description = item.description.value
        db_item.price = item.price.value
        db_item.updated_by = item.updated_by.value
        db_item.updated_at = datetime.now(tz=jst)

        await self.session.flush()
        # await self.session.refresh(db_item)
        await self.session.commit()
        return ItemEntity.model_validate(db_item)

    async def delete(self, item: ItemEntity) -> bool:
        """商品を論理削除"""
        result = await self.session.execute(
            select(ItemModel).where(
                ItemModel.id == item.id,
                ItemModel.deleted_at.is_(None)
            )
        )
        db_item = result.scalar_one_or_none()
        
        if not db_item:
            return False

        db_item.updated_at = datetime.now(tz=jst)
        db_item.deleted_at = datetime.now(tz=jst)
        await self.session.flush()
        await self.session.commit()
        return True

    # 以下、旧ItemCategoryRepositoryから移動したメソッド
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
                existing.updated_at = datetime.now(tz=jst)
                await self.session.flush()
                return True
            return True

        # 新規作成
        db_item_category = ItemCategoryModel(
            item_id=item_id,
            category_id=category_id,
            created_by=created_by,
            created_at=datetime.now(tz=jst),
            updated_by=updated_by,
            updated_at=datetime.now(tz=jst)
        )
        self.session.add(db_item_category)
        await self.session.flush()
        # await self.session.refresh(db_item_category)
        await self.session.commit()
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

        db_item_category.deleted_at = datetime.now(tz=jst)
        await self.session.flush()
        await self.session.commit()
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
        return [CategoryEntity.model_validate(category, from_attributes=True) for category in db_categories]
