"""
リポジトリインターフェース（抽象）
ドメイン層でインターフェースを定義し、インフラ層で実装する（依存性逆転の原則）
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from .entity import ItemEntity


class AbstractItemRepository(ABC):
    """商品リポジトリインターフェース"""

    @abstractmethod
    async def create(self, item: ItemEntity) -> ItemEntity:
        """商品を作成"""
        pass

    @abstractmethod
    async def find_by_id(self, item_id: int) -> Optional[ItemEntity]:
        """IDで商品を検索"""
        pass

    @abstractmethod
    async def find_all(self, skip: int = 0, limit: int = 100) -> List[ItemEntity]:
        """全商品を取得"""
        pass

    @abstractmethod
    async def update(self, item_id: int, item: ItemEntity) -> Optional[ItemEntity]:
        """商品を更新"""
        pass

    @abstractmethod
    async def delete(self, item_id: int) -> bool:
        """商品を論理削除"""
        pass