"""
ユーザー作成ユースケース
"""

from domain import UserEntity
from application.services.user_service import UserService


class CreateUserUseCase:
    """ユーザー作成ユースケース"""

    def __init__(self, user_service: UserService):
        """
        Args:
            user_service: ユーザーサービス
        """
        self.user_service = user_service

    async def __call__(
        self,
        name: str,
        email: str,
        password: str,
        admin: bool,
        created_by: str
    ) -> UserEntity:
        """
        ユーザーを作成する
        
        Args:
            name: ユーザー名
            email: メールアドレス
            password: パスワード
            admin: 管理者フラグ
            created_by: 作成者
            
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
            created_by=created_by
        )
        
        return user
