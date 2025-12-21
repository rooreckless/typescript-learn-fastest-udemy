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


class ItemEntity(BaseModel):
    """商品エンティティ"""
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., max_length=200)
    price: int = Field(..., ge=0)
    created_by: str = Field(..., max_length=45)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: str = Field(..., max_length=45)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True


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


class ItemCategoryEntity(BaseModel):
    """商品カテゴリ関連エンティティ"""
    item_id: int
    category_id: int
    created_by: str = Field(..., max_length=45)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: str = Field(..., max_length=45)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ItemWithCategories(BaseModel):
    """カテゴリ情報付き商品エンティティ（集約ルート）"""
    item: ItemEntity
    categories: List[CategoryEntity] = []

    class Config:
        from_attributes = True
