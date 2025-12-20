"""
=========================================
FastAPI メインアプリケーション
=========================================
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from datetime import datetime

# FastAPIアプリケーションのインスタンス作成
app = FastAPI(
    title="NAFP API",
    description="Nginx-Angular-FastAPI-PostgreSQL Stack API",
    version="1.0.0",
    docs_url="/api/docs",  # Swagger UIのURL
    redoc_url="/api/redoc",  # ReDocのURL
)

# =========================================
# CORS設定（開発環境用）
# =========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",  # Angular開発サーバー
        "http://localhost:80",     # Nginx
        "http://localhost",
    ],
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)

# =========================================
# データモデル
# =========================================
class User(BaseModel):
    """ユーザーモデル"""
    id: Optional[int] = None
    username: str
    email: str
    created_at: Optional[datetime] = None

class HealthResponse(BaseModel):
    """ヘルスチェックレスポンスモデル"""
    status: str
    timestamp: datetime
    environment: str

# =========================================
# エンドポイント
# =========================================

@app.get("/", tags=["Root"])
async def root():
    """
    ルートエンドポイント
    APIの基本情報を返す
    """
    return {
        "message": "Welcome to NAFP API",
        "version": "1.0.0",
        "docs": "/api/docs",
    }

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    ヘルスチェックエンドポイント
    アプリケーションの状態を確認
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(),
        environment=os.getenv("ENVIRONMENT", "unknown"),
    )

@app.get("/api/users", response_model=List[User], tags=["Users"])
async def get_users():
    """
    ユーザー一覧取得エンドポイント
    
    TODO: データベースからの取得に変更する
    現在はダミーデータを返している
    """
    # ダミーデータ
    dummy_users = [
        User(
            id=1,
            username="admin",
            email="admin@example.com",
            created_at=datetime.now(),
        ),
        User(
            id=2,
            username="user1",
            email="user1@example.com",
            created_at=datetime.now(),
        ),
    ]
    return dummy_users

@app.get("/api/users/{user_id}", response_model=User, tags=["Users"])
async def get_user(user_id: int):
    """
    ユーザー詳細取得エンドポイント
    
    Args:
        user_id: ユーザーID
    
    Returns:
        User: ユーザー情報
    
    Raises:
        HTTPException: ユーザーが見つからない場合
    """
    # ダミーデータ
    if user_id == 1:
        return User(
            id=1,
            username="admin",
            email="admin@example.com",
            created_at=datetime.now(),
        )
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/api/users", response_model=User, tags=["Users"])
async def create_user(user: User):
    """
    ユーザー作成エンドポイント
    
    Args:
        user: 作成するユーザー情報
    
    Returns:
        User: 作成されたユーザー情報
    
    TODO: データベースへの保存を実装する
    """
    # ダミーレスポンス
    user.id = 999
    user.created_at = datetime.now()
    return user

# =========================================
# アプリケーション起動イベント
# =========================================
@app.on_event("startup")
async def startup_event():
    """
    アプリケーション起動時の処理
    データベース接続の初期化など
    """
    print("🚀 FastAPI application is starting up...")
    print(f"📝 Environment: {os.getenv('ENVIRONMENT', 'unknown')}")
    print(f"🔗 Database URL: {os.getenv('DATABASE_URL', 'not set')}")

@app.on_event("shutdown")
async def shutdown_event():
    """
    アプリケーション終了時の処理
    データベース接続のクローズなど
    """
    print("👋 FastAPI application is shutting down...")
