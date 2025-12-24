"""
ドメインエンティティ
ビジネスルールと永続化されるエンティティを定義
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from .value_objects import UserName, UserEmail, UserPasswordHash, UserCreatedBy, UserUpdatedBy


class UserEntity(BaseModel):
    """ユーザーエンティティ"""
    id: Optional[int] = None
    name: UserName
    password_hash: UserPasswordHash
    email: UserEmail
    admin: bool = Field(default=False)
    created_by: UserCreatedBy
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: UserUpdatedBy
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True