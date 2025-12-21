from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# =========================================
# 商品関連スキーマ
# =========================================

class ItemCreateRequest(BaseModel):
    """商品作成リクエスト"""
    name: str = Field(..., min_length=1, max_length=100, description="商品名")
    description: str = Field(..., max_length=200, description="商品説明")
    price: int = Field(..., ge=0, description="価格")
    created_by: str = Field(default="system", description="作成者")


class ItemUpdateRequest(BaseModel):
    """商品更新リクエスト"""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="商品名")
    description: Optional[str] = Field(None, max_length=200, description="商品説明")
    price: Optional[int] = Field(None, ge=0, description="価格")
    updated_by: str = Field(default="system", description="更新者")


class ItemResponse(BaseModel):
    """商品レスポンス"""
    id: int
    name: str
    description: str
    price: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True