"""
ユーザー全取得ユースケース
"""

from typing import List
from domain import UserEntity
from application.services.user_service import UserService


class GetAllUsersUseCase:
    """ユーザー全取得ユースケース"""

    def __init__(self, user_service: UserService):
        """
        Args:
            user_service: ユーザーサービス
        """
        self.user_service = user_service

    async def __call__(
        self,
        skip: int = 0,
        limit: int = 100
    ) -> List[UserEntity]:
        """
        ユーザーをすべて取得する
        
        Args:
            skip: スキップする件数
            limit: 取得する最大件数
            
        Returns:
            取得したユーザーのリスト
        """
        # ユーザーをすべて取得
        users = await self.user_service.get_all_users(skip=skip, limit=limit)
        
        return users
