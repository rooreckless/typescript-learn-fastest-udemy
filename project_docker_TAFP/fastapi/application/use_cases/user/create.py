"""
ユーザー作成ユースケース
"""

from domain import UserEntity
from application.services.user_service import UserService


class CreateUserUseCase:
    """ユーザー作成ユースケース"""

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
        name: str,
        email: str,
        password: str,
        admin: bool
    ) -> UserEntity:
        """
        ユーザーを作成する
        
        Args:
            name: ユーザー名
            email: メールアドレス
            password: パスワード
            admin: 管理者フラグ
            
        Returns:
            作成されたユーザーエンティティ
            
        Raises:
            ValueError: バリデーションエラー
        """
        # ユーザーを作成
        user = await self.user_service.create_user(
            name=name,
            email=email,
            password=password,
            admin=admin,
            created_by=self.current_user.name.value
        )
        
        return user
