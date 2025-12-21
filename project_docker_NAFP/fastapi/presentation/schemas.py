"""
プレゼンテーション層のスキーマ定義
リクエスト/レスポンスモデル
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime


# =========================================
# ユーザー関連スキーマ
# =========================================

class UserCreateRequest(BaseModel):
    """ユーザー作成リクエスト"""
    name: str = Field(..., min_length=1, max_length=45, description="ユーザー名")
    email: EmailStr = Field(..., description="メールアドレス")
    password: str = Field(..., min_length=8, description="パスワード")
    admin: bool = Field(default=False, description="管理者フラグ")
    created_by: str = Field(default="system", description="作成者")


class UserUpdateRequest(BaseModel):
    """ユーザー更新リクエスト"""
    name: Optional[str] = Field(None, min_length=1, max_length=45, description="ユーザー名")
    email: Optional[EmailStr] = Field(None, description="メールアドレス")
    password: Optional[str] = Field(None, min_length=8, description="パスワード")
    admin: Optional[bool] = Field(None, description="管理者フラグ")
    updated_by: str = Field(default="system", description="更新者")


class UserResponse(BaseModel):
    """ユーザーレスポンス"""
    id: int
    name: str
    email: str
    admin: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


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


# =========================================
# カテゴリ関連スキーマ
# =========================================

class CategoryCreateRequest(BaseModel):
    """カテゴリ作成リクエスト"""
    name: str = Field(..., min_length=1, max_length=100, description="カテゴリ名")
    description: str = Field(..., max_length=200, description="カテゴリ説明")
    created_by: str = Field(default="system", description="作成者")


class CategoryUpdateRequest(BaseModel):
    """カテゴリ更新リクエスト"""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="カテゴリ名")
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


# =========================================
# 商品カテゴリ関連スキーマ
# =========================================

class ItemCategoryRequest(BaseModel):
    """商品カテゴリ関連リクエスト"""
    item_id: int = Field(..., description="商品ID")
    category_id: int = Field(..., description="カテゴリID")
    created_by: str = Field(default="system", description="作成者")


class ItemWithCategoriesResponse(BaseModel):
    """カテゴリ情報付き商品レスポンス"""
    item: ItemResponse
    categories: List[CategoryResponse] = []

    class Config:
        from_attributes = True


# =========================================
# 汎用レスポンス
# =========================================

class MessageResponse(BaseModel):
    """メッセージレスポンス"""
    message: str
    success: bool = True


class ErrorResponse(BaseModel):
    """エラーレスポンス"""
    detail: str
    status_code: int


# =========================================
# 認証関連スキーマ
# =========================================

class LoginRequest(BaseModel):
    """ログインリクエスト"""
    email: EmailStr = Field(..., description="メールアドレス")
    password: str = Field(..., min_length=1, description="パスワード")


class LoginResponse(BaseModel):
    """ログインレスポンス"""
    access_token: str = Field(..., description="アクセストークン")
    token_type: str = Field(default="bearer", description="トークンタイプ")
    user: UserResponse = Field(..., description="ユーザー情報")
