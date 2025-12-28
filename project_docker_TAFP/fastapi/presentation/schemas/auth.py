from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from .users import UserResponse

# =========================================
# 認証関連スキーマ
# =========================================

class LoginRequest(BaseModel):
    """ログインリクエスト"""
    email: EmailStr = Field(..., description="メールアドレス")
    password: str = Field(..., min_length=1, description="パスワード")


class LoginResponse(BaseModel):
    """ログインレスポンス"""
    access_token: str = Field(..., description="アクセストークン")
    token_type: str = Field(default="bearer", description="トークンタイプ")
    user: UserResponse = Field(..., description="ユーザー情報")