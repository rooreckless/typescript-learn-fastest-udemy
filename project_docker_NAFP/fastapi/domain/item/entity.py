"""
ドメインエンティティ
ビジネスルールと永続化されるエンティティを定義
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from .value_objects import ItemName, ItemDescription, ItemPrice, ItemCreatedBy, ItemUpdatedBy


class ItemEntity(BaseModel):
    """商品エンティティ"""
    id: Optional[int] = None
    name: ItemName
    description: ItemDescription
    price: ItemPrice
    created_by: ItemCreatedBy
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: ItemUpdatedBy
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

from ..category.entity import CategoryEntity
class ItemWithCategories(BaseModel):
    """カテゴリ情報付き商品エンティティ（集約ルート）"""
    item: ItemEntity
    categories: List[CategoryEntity] = []

    class Config:
        from_attributes = True