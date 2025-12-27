"""
ユーザーID取得ユースケース
"""

from typing import Optional
from domain import UserEntity
from application.services.user_service import UserService


class GetUserByIdUseCase:
    """ユーザーID取得ユースケース"""

    def __init__(self, user_service: UserService):
        """
        Args:
            user_service: ユーザーサービス
        """
        self.user_service = user_service

    async def __call__(
        self,
        user_id: int
    ) -> Optional[UserEntity]:
        """
        IDでユーザーを取得する
        
        Args:
            user_id: ユーザーID
            
        Returns:
            取得したユーザーエンティティ、存在しない場合はNone
        """
        # IDでユーザーを取得
        user = await self.user_service.get_user_by_id(user_id)
        
        return user
