"""
ドメインエンティティ
ビジネスルールと永続化されるエンティティを定義
"""

from datetime import datetime
from typing import Optional, List, Union
from pydantic import BaseModel, Field, EmailStr, field_validator
from .value_objects import Name
from typing import Self

class CategoryEntity(BaseModel):
    """カテゴリエンティティ"""
    id: Optional[int] = None
    name: str  # 常に文字列として扱う
    description: str = Field(..., max_length=200)
    created_by: str = Field(..., max_length=45)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: str = Field(..., max_length=45)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    
    @classmethod
    def create(
        cls,
        name: str,
        description: str,
        created_by: str,
        updated_by: str
    ) -> Self:
        """
        新しいカテゴリを作成
        
        Args:
            name: カテゴリ名（文字列）
            description: カテゴリ説明
            created_by: 作成者
            updated_by: 更新者
            
        Returns:
            作成されたカテゴリエンティティ
        """
        # field_validatorにより自動的にstrからNameに変換される
        category = cls(
            name=name,  # ここでは文字列を渡すだけでOK
            description=description,
            created_by=created_by,
            updated_by=updated_by
        )
        return category


from ..item.entity import ItemEntity
class CategoryWithItems(BaseModel):
    """商品情報付きカテゴリエンティティ（集約ルート）"""
    category: CategoryEntity
    items: List[ItemEntity] = []

    class Config:
        from_attributes = True