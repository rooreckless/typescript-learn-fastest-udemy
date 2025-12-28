"""
リポジトリインターフェース（抽象）
ドメイン層でインターフェースを定義し、インフラ層で実装する（依存性逆転の原則）
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from .entity import UserEntity


class AbstractUserRepository(ABC):
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