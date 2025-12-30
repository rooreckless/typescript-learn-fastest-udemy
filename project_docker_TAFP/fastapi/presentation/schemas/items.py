from pydantic import BaseModel, Field, field_serializer, model_validator
from typing import Optional, List, Any
from datetime import datetime


# =========================================
# 商品関連スキーマ
# =========================================

class ItemCreateRequest(BaseModel):
    """商品作成リクエスト"""
    name: str = Field(..., min_length=1, max_length=100, description="商品名")
    description: str = Field(..., max_length=200, description="商品説明")
    price: int = Field(..., ge=0, description="価格")


class ItemUpdateRequest(BaseModel):
    """商品更新リクエスト"""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="商品名")
    description: Optional[str] = Field(None, max_length=200, description="商品説明")
    price: Optional[int] = Field(None, ge=0, description="価格")


class ItemResponse(BaseModel):
    """商品レスポンス"""
    id: int
    name: str
    description: str
    price: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str
    deleted_at: Optional[datetime] = None

    @model_validator(mode='before')
    @classmethod
    def convert_value_objects(cls, data: Any) -> Any:
        """値オブジェクトを適切な型に変換"""
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