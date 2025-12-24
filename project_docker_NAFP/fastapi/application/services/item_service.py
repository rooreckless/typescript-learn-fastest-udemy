"""
商品ユースケース（アプリケーションサービス）
"""

from typing import List, Optional

from domain import ItemEntity,ItemWithCategories,AbstractItemRepository


class ItemService:
    """商品サービスクラス"""

    def __init__(
        self,
        item_repository: AbstractItemRepository
    ):
        self.item_repository = item_repository

    async def create_item(
        self,
        name: str,
        description: str,
        price: int,
        created_by: str
    ) -> ItemEntity:
        """
        新しい商品を作成
        
        Args:
            name: 商品名
            description: 商品説明
            price: 価格
            created_by: 作成者
            
        Returns:
            作成された商品エンティティ
        """
        item = ItemEntity(
            name=name,
            description=description,
            price=price,
            created_by=created_by,
            updated_by=created_by
        )
        return await self.item_repository.create(item)

    async def get_item_by_id(self, item_id: int) -> Optional[ItemEntity]:
        """IDで商品を取得"""
        return await self.item_repository.find_by_id(item_id)

    async def get_item_with_categories(self, item_id: int) -> Optional[ItemWithCategories]:
        """カテゴリ情報付きで商品を取得"""
        item = await self.item_repository.find_by_id(item_id)
        if not item:
            return None

        categories = await self.item_repository.find_categories_by_item(item_id)
        return ItemWithCategories(item=item, categories=categories)

    async def get_all_items(self, skip: int = 0, limit: int = 100) -> List[ItemEntity]:
        """全商品を取得"""
        return await self.item_repository.find_all(skip, limit)

    async def update_item(
        self,
        item_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[int] = None,
        updated_by: str = "system"
    ) -> Optional[ItemEntity]:
        """
        商品情報を更新
        
        Args:
            item_id: 商品ID
            name: 新しい商品名（オプション）
            description: 新しい商品説明（オプション）
            price: 新しい価格（オプション）
            updated_by: 更新者
            
        Returns:
            更新された商品エンティティ
        """
        existing_item = await self.item_repository.find_by_id(item_id)
        if not existing_item:
            return None

        updated_item = ItemEntity(
            id=item_id,
            name=name if name else existing_item.name,
            description=description if description else existing_item.description,
            price=price if price is not None else existing_item.price,
            created_by=existing_item.created_by,
            created_at=existing_item.created_at,
            updated_by=updated_by
        )

        return await self.item_repository.update(item_id, updated_item)

    async def delete_item(self, item_id: int) -> bool:
        """商品を論理削除"""
        return await self.item_repository.delete(item_id)

