"""
ドメインエンティティ
ビジネスルールと永続化されるエンティティを定義
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr


class UserEntity(BaseModel):
    """ユーザーエンティティ"""
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=45)
    password_hash: str
    email: EmailStr = Field(..., max_length=255)
    admin: bool = Field(default=False)
    created_by: str = Field(..., max_length=45)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: str = Field(..., max_length=45)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True