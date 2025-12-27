"""
プレゼンテーション層のスキーマ定義
リクエスト/レスポンスモデル
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime



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



