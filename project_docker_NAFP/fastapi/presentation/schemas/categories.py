from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
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

    class Config:
        from_attributes = True