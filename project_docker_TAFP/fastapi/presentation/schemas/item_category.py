from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .items import ItemResponse
from .categories import CategoryResponse




# =========================================
# 商品カテゴリ関連スキーマ
# =========================================

class ItemCategoryRequest(BaseModel):
    """商品カテゴリ関連リクエスト"""
    item_id: int = Field(..., description="商品ID")
    category_id: int = Field(..., description="カテゴリID")


class ItemWithCategoriesResponse(BaseModel):
    """カテゴリ情報付き商品レスポンス"""
    item: ItemResponse
    categories: List[CategoryResponse] = []

    class Config:
        from_attributes = True