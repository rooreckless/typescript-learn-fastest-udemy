"""
商品リポジトリ実装
"""

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime

from domain.item import ItemEntity
from domain.repositories import IItemRepository
from infrastructure.models import ItemModel


class ItemRepository(IItemRepository):
    """商品リポジトリ実装クラス"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, item: ItemEntity) -> ItemEntity:
        """商品を作成"""
        db_item = ItemModel(
            name=item.name,
            description=item.description,
            price=item.price,
            created_by=item.created_by,
            updated_by=item.updated_by,
        )
        self.session.add(db_item)
        await self.session.flush()
        await self.session.refresh(db_item)
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

    async def update(self, item_id: int, item: ItemEntity) -> Optional[ItemEntity]:
        """商品を更新"""
        result = await self.session.execute(
            select(ItemModel).where(
                ItemModel.id == item_id,
                ItemModel.deleted_at.is_(None)
            )
        )
        db_item = result.scalar_one_or_none()
        
        if not db_item:
            return None

        db_item.name = item.name
        db_item.description = item.description
        db_item.price = item.price
        db_item.updated_by = item.updated_by
        db_item.updated_at = datetime.now()

        await self.session.flush()
        await self.session.refresh(db_item)
        return ItemEntity.model_validate(db_item)

    async def delete(self, item_id: int) -> bool:
        """商品を論理削除"""
        result = await self.session.execute(
            select(ItemModel).where(
                ItemModel.id == item_id,
                ItemModel.deleted_at.is_(None)
            )
        )
        db_item = result.scalar_one_or_none()
        
        if not db_item:
            return False

        db_item.deleted_at = datetime.now()
        await self.session.flush()
        return True
