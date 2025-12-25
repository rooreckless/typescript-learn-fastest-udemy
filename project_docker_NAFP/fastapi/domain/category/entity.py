"""
ドメインエンティティ
ビジネスルールと永続化されるエンティティを定義
"""

from datetime import datetime
from typing import Optional, List, Union, Dict, Any
from pydantic import BaseModel, Field, field_validator, model_serializer
from .value_objects import Name, Description, CreatedBy, UpdatedBy
from typing import Self

class CategoryEntity(BaseModel):
    """カテゴリエンティティ"""
    id: Optional[int] = None
    name: Name  # Name値オブジェクト
    description: Description  # Description値オブジェクト
    created_by: CreatedBy  # CreatedBy値オブジェクト
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: UpdatedBy  # UpdatedBy値オブジェクト
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
            description: カテゴリ説明（文字列）
            created_by: 作成者（文字列）
            updated_by: 更新者（文字列）
            
        Returns:
            作成されたカテゴリエンティティ
        """
        # field_validatorにより自動的にstrから各値オブジェクトに変換される
        category = cls(
            name=Name.validate_value(name),
            description=Description.validate_value(description),
            created_by=CreatedBy.validate_value(created_by),
            updated_by=UpdatedBy.validate_value(updated_by)
        )
        return category


from ..item.entity import ItemEntity
class CategoryWithItems(BaseModel):
    """商品情報付きカテゴリエンティティ（集約ルート）"""
    category: CategoryEntity
    items: List[ItemEntity] = []

    class Config:
        from_attributes = True