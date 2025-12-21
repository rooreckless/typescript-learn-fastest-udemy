"""
リポジトリインターフェース（抽象）
ドメイン層でインターフェースを定義し、インフラ層で実装する（依存性逆転の原則）
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from domain import UserEntity,ItemEntity,CategoryEntity



class AbstractItemCategoryRepository(ABC):
    """商品カテゴリ関連リポジトリインターフェース"""

    @abstractmethod
    async def add_category_to_item(
        self, 
        item_id: int, 
        category_id: int, 
        created_by: str, 
        updated_by: str
    ) -> bool:
        """商品にカテゴリを追加"""
        pass

    @abstractmethod
    async def remove_category_from_item(self, item_id: int, category_id: int) -> bool:
        """商品からカテゴリを削除"""
        pass

    @abstractmethod
    async def find_categories_by_item(self, item_id: int) -> List[CategoryEntity]:
        """商品に紐づくカテゴリを取得"""
        pass

    @abstractmethod
    async def find_items_by_category(self, category_id: int) -> List[ItemEntity]:
        """カテゴリに紐づく商品を取得"""
        pass
