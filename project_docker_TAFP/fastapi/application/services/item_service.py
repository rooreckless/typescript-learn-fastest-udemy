"""
商品ユースケース（アプリケーションサービス）
"""

from typing import List, Optional

from domain import ItemEntity,ItemWithCategories,AbstractItemRepository,UserEntity


class ItemService:
    """商品サービスクラス"""

    def __init__(
        self,
        item_repository: AbstractItemRepository
    ):
        self.item_repository = item_repository

    async def create_item(
        self,
        item: ItemEntity
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
        item: ItemEntity,
    ) -> Optional[ItemEntity]:
        """
        商品情報を更新
        
        Args:
            item: 更新する商品エンティティ
            
        Returns:
            更新された商品エンティティ
        """

        return await self.item_repository.update(item)

    async def delete_item(self, item: ItemEntity, current_user: UserEntity) -> bool:
        """商品を論理削除
        
        Args:
            item: 削除する商品エンティティ
            current_user: 現在のログインユーザー
            
        Returns:
            削除が成功した場合True
        """
        item.delete(updated_by=current_user.name.value)
        await self.item_repository.update(item)
        return True

