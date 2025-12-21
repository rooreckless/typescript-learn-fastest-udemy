"""
リポジトリインターフェース（抽象）
ドメイン層でインターフェースを定義し、インフラ層で実装する（依存性逆転の原則）
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from .entity import CategoryEntity


class AbstractCategoryRepository(ABC):
    """カテゴリリポジトリインターフェース"""

    @abstractmethod
    async def create(self, category: CategoryEntity) -> CategoryEntity:
        """カテゴリを作成"""
        pass

    @abstractmethod
    async def find_by_id(self, category_id: int) -> Optional[CategoryEntity]:
        """IDでカテゴリを検索"""
        pass

    @abstractmethod
    async def find_all(self, skip: int = 0, limit: int = 100) -> List[CategoryEntity]:
        """全カテゴリを取得"""
        pass

    @abstractmethod
    async def update(self, category_id: int, category: CategoryEntity) -> Optional[CategoryEntity]:
        """カテゴリを更新"""
        pass

    @abstractmethod
    async def delete(self, category_id: int) -> bool:
        """カテゴリを論理削除"""
        pass