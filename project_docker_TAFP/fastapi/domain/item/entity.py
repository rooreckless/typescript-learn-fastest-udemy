"""
ドメインエンティティ
ビジネスルールと永続化されるエンティティを定義
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from .value_objects import Name, Description, Price, CreatedBy, UpdatedBy


class ItemEntity(BaseModel):
    """商品エンティティ"""
    id: Optional[int] = None
    name: Name
    description: Description
    price: Price
    created_by: CreatedBy
    created_at: datetime = Field(default_factory=datetime.now)
    updated_by: UpdatedBy
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

    @classmethod
    def create(cls,
               name: str,
        description: str,
        price: int,
        created_by: str,
        updated_by: str
    ) -> "ItemEntity":
        """
        新しい商品を作成
        
        Args:
            name: 商品名（文字列）
            description: 商品説明（文字列）
            price: 価格（整数）
            created_by: 作成者（文字列）
            updated_by: 更新者（文字列）
        """
        # field_validatorにより自動的にstrから各値オブジェクトに変換される
        item = cls(
            name=Name.validate_value(name),
            description=Description.validate_value(description),
            price=Price.validate_value(price),
            created_by=CreatedBy.validate_value(created_by),
            updated_by=UpdatedBy.validate_value(updated_by)
        )
        return item

    def update(
        self,
        name: str = None,
        description: str = None,
        price: int = None,
        updated_by: str = "system"
    ) -> "ItemEntity":
        """
        既存の商品を更新
        
        Args:
            name: 新しい商品名（オプション）
            description: 新しい商品説明（オプション）
            price: 新しい価格（オプション）
            updated_by: 更新者（文字列、オプション)
        """

        self.name = Name(value=name) if name is not None else self.name
        self.description = Description(value=description) if description is not None else self.description
        self.price = Price(value=price) if price is not None else self.price
        self.updated_by = UpdatedBy(value=updated_by)
        self.updated_at = datetime.now()

        return self

    def delete(self, updated_by: str = "system") -> "ItemEntity":
        """商品を論理削除
        
        Args:
            updated_by: 更新者（文字列、オプション）
        """
        self.deleted_at = datetime.now()
        self.updated_by = UpdatedBy(value=updated_by)
        self.updated_at = datetime.now()
        return self

from ..category.entity import CategoryEntity
class ItemWithCategories(BaseModel):
    """カテゴリ情報付き商品エンティティ（集約ルート）"""
    item: ItemEntity
    categories: List[CategoryEntity] = []

    class Config:
        from_attributes = True