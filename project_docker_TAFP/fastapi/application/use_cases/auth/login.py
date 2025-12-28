"""
ログインユースケース
"""

from datetime import timedelta
from typing import Optional
from domain import UserEntity
from application.services.user_service import UserService
from presentation.schemas import LoginRequest, LoginResponse, UserResponse
from presentation.auth import create_access_token, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES


class LoginUseCase:
    """ログインユースケース"""

    def __init__(self, user_service: UserService):
        """
        Args:
            user_service: ユーザーサービス
        """
        self.user_service = user_service

    async def __call__(
        self,
        request: LoginRequest
    ) -> Optional[tuple[str, UserEntity]]:
        """
        ユーザー認証を行い、JWTトークンを発行する
        
        Args:
            request: ログインリクエスト
            
        Returns:
            (アクセストークン, ユーザーエンティティ) のタプル、認証失敗時はNone
        """
        # メールアドレスでユーザーを検索
        user = await self.user_service.get_user_by_email(request.email)
        
        if not user:
            return None
        
        # パスワードを検証
        if not verify_password(request.password, str(user.password_hash)):
            return None
        
        # JWTトークンを生成
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={
                "sub": str(user.id),
                "email": str(user.email),
                "admin": user.admin
            },
            expires_delta=access_token_expires
        )
        
        return access_token, user
