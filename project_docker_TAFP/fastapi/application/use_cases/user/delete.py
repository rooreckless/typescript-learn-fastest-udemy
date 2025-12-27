"""
ユーザー削除ユースケース
"""

from application.services.user_service import UserService


class DeleteUserUseCase:
    """ユーザー削除ユースケース"""

    def __init__(self, user_service: UserService):
        """
        Args:
            user_service: ユーザーサービス
        """
        self.user_service = user_service

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
        success = await self.user_service.delete_user(user_id)
        
        return success
