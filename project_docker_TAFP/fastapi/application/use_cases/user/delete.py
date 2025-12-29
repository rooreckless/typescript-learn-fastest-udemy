"""
ユーザー削除ユースケース
"""

from application.services.user_service import UserService
from domain import UserEntity


class DeleteUserUseCase:
    """ユーザー削除ユースケース"""

    def __init__(self, user_service: UserService, current_user: UserEntity):
        """
        Args:
            user_service: ユーザーサービス
            current_user: 現在のログインユーザー
        """
        self.user_service = user_service
        self.current_user = current_user

    async def __call__(
        self,
        user_id: int
    ) -> bool:
        """
        ユーザーを論理削除する
        
        Args:
            user_id: ユーザーID
            
        Returns:
            削除が成功した場合True、失敗した場合False
        """
        # ユーザーを削除
        success = await self.user_service.delete_user(user_id, self.current_user)
        
        return success
