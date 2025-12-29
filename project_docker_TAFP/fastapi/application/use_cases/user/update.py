"""
ユーザー更新ユースケース
"""

from typing import Optional
from domain import UserEntity
from application.services.user_service import UserService


class UpdateUserUseCase:
    """ユーザー更新ユースケース"""

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
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        admin: Optional[bool] = None
    ) -> Optional[UserEntity]:
        """
        ユーザーを更新する
        
        Args:
            user_id: ユーザーID
            name: 新しいユーザー名（オプション）
            email: 新しいメールアドレス（オプション）
            password: 新しいパスワード（オプション）
            admin: 管理者フラグ（オプション）
            
        Returns:
            更新されたユーザーエンティティ、存在しない場合はNone
            
        Raises:
            ValueError: バリデーションエラー
        """
        # ユーザーを更新
        user = await self.user_service.update_user(
            user_id=user_id,
            name=name,
            email=email,
            password=password,
            admin=admin,
            updated_by=self.current_user.name.value
        )
        
        return user
