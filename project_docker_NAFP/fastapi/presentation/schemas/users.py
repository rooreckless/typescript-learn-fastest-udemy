from pydantic import BaseModel, Field, EmailStr, field_serializer, model_validator
from typing import Optional, List, Any
from datetime import datetime


# =========================================
# ユーザー関連スキーマ
# =========================================

class UserCreateRequest(BaseModel):
    """ユーザー作成リクエスト"""
    name: str = Field(..., min_length=1, max_length=45, description="ユーザー名")
    email: EmailStr = Field(..., description="メールアドレス")
    password: str = Field(..., min_length=8, description="パスワード")
    admin: bool = Field(default=False, description="管理者フラグ")
    created_by: str = Field(default="system", description="作成者")


class UserUpdateRequest(BaseModel):
    """ユーザー更新リクエスト"""
    name: Optional[str] = Field(None, min_length=1, max_length=45, description="ユーザー名")
    email: Optional[EmailStr] = Field(None, description="メールアドレス")
    password: Optional[str] = Field(None, min_length=8, description="パスワード")
    admin: Optional[bool] = Field(None, description="管理者フラグ")
    updated_by: str = Field(default="system", description="更新者")


class UserResponse(BaseModel):
    """ユーザーレスポンス"""
    id: int
    name: str
    email: str
    admin: bool
    created_at: datetime
    updated_at: datetime

    @model_validator(mode='before')
    @classmethod
    def convert_value_objects(cls, data: Any) -> Any:
        """値オブジェクトを文字列に変換"""
        if hasattr(data, '__dict__'):
            data_dict = {}
            for key, value in data.__dict__.items():
                if hasattr(value, 'value'):
                    data_dict[key] = value.value
                else:
                    data_dict[key] = value
            return data_dict
        return data

    class Config:
        from_attributes = True