"""
リポジトリインターフェース（抽象）
ドメイン層でインターフェースを定義し、インフラ層で実装する（依存性逆転の原則）
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from .entity import ItemEntity

# 循環インポート回避のTYPE_CHECKING
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..category.entity import CategoryEntity


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
    async def update(self, item: ItemEntity) -> Optional[ItemEntity]:
        """商品を更新"""
        pass

    @abstractmethod
    async def delete(self, item_id: int) -> bool:
        """商品を論理削除"""
        pass

    # 以下、旧AbstractItemCategoryRepositoryから移動
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
    async def find_categories_by_item(self, item_id: int) -> List['CategoryEntity']:
        """商品に紐づくカテゴリを取得"""
        pass