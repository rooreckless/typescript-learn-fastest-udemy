from pydantic import BaseModel, Field, EmailStr, field_serializer, model_validator
from typing import Optional, List, Any
from datetime import datetime


# =========================================
# カテゴリ関連スキーマ
# =========================================

class CategoryCreateRequest(BaseModel):
    """カテゴリ作成リクエスト"""
    name: str = Field(..., min_length=1, max_length=200, description="カテゴリ名")
    description: str = Field(..., max_length=200, description="カテゴリ説明")
    created_by: str = Field(default="system", description="作成者")


class CategoryUpdateRequest(BaseModel):
    """カテゴリ更新リクエスト"""
    name: Optional[str] = Field(None, min_length=1, max_length=200, description="カテゴリ名")
    description: Optional[str] = Field(None, max_length=200, description="カテゴリ説明")
    updated_by: str = Field(default="system", description="更新者")


class CategoryResponse(BaseModel):
    """カテゴリレスポンス"""
    id: int
    name: str
    description: str
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