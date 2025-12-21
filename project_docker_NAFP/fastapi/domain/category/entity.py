"""
ドメインエンティティ
ビジネスルールと永続化されるエンティティを定義
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr



class CategoryEntity(BaseModel):
    """カテゴリエンティティ"""
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., max_length=200)
    created_by: str = Field(..., max_length=45)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: str = Field(..., max_length=45)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True