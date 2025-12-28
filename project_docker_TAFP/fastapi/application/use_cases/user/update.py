"""
ユーザー更新ユースケース
"""

from typing import Optional
from domain import UserEntity
from application.services.user_service import UserService


class UpdateUserUseCase:
    """ユーザー更新ユースケース"""

    def __init__(self, user_service: UserService):
        """
        Args:
            user_service: ユーザーサービス
        """
        self.user_service = user_service

    async def __call__(
        self,
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        admin: Optional[bool] = None,
        updated_by: Optional[str] = None
    ) -> Optional[UserEntity]:
        """
        ユーザーを更新する
        
        Args:
            user_id: ユーザーID
            name: 新しいユーザー名（オプション）
            email: 新しいメールアドレス（オプション）
            password: 新しいパスワード（オプション）
            admin: 管理者フラグ（オプション）
            updated_by: 更新者
            
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
            updated_by=updated_by
        )
        
        return user
