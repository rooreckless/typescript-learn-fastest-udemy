"""
リポジトリインターフェース（抽象）
ドメイン層でインターフェースを定義し、インフラ層で実装する（依存性逆転の原則）
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities import UserEntity, ItemEntity, CategoryEntity, ItemCategoryEntity


class IUserRepository(ABC):
    """ユーザーリポジトリインターフェース"""

    @abstractmethod
    async def create(self, user: UserEntity) -> UserEntity:
        """ユーザーを作成"""
        pass

    @abstractmethod
    async def find_by_id(self, user_id: int) -> Optional[UserEntity]:
        """IDでユーザーを検索"""
        pass

    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[UserEntity]:
        """メールアドレスでユーザーを検索"""
        pass

    @abstractmethod
    async def find_all(self, skip: int = 0, limit: int = 100) -> List[UserEntity]:
        """全ユーザーを取得"""
        pass

    @abstractmethod
    async def update(self, user_id: int, user: UserEntity) -> Optional[UserEntity]:
        """ユーザーを更新"""
        pass

    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        """ユーザーを論理削除"""
        pass


class IItemRepository(ABC):
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


class ICategoryRepository(ABC):
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


class IItemCategoryRepository(ABC):
    """商品カテゴリ関連リポジトリインターフェース"""

    @abstractmethod
    async def add_category_to_item(self, item_category: ItemCategoryEntity) -> ItemCategoryEntity:
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
