"""
=========================================
FastAPI メインアプリケーション
ドメイン駆動設計（DDD）に基づいたCRUD API
=========================================
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from infrastructure.database import init_db
from presentation.user_routes import router as user_router
from presentation.item_routes import router as item_router
from presentation.category_routes import router as category_router


# =========================================
# アプリケーションライフサイクルイベント
# =========================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """起動時・終了時の処理"""
    # 起動時: データベース初期化
    # await init_db()  # 既にSQLファイルで初期化されるためコメントアウト
    print("🚀 FastAPI application started")
    yield
    # 終了時の処理
    print("🛑 FastAPI application stopped")


# =========================================
# FastAPIアプリケーションのインスタンス作成
# =========================================
app = FastAPI(
    title="NAFP API",
    description="Nginx-Angular-FastAPI-PostgreSQL Stack API (Domain-Driven Design)",
    version="2.0.0",
    docs_url="/api/docs",  # Swagger UIのURL
    redoc_url="/api/redoc",  # ReDocのURL
    lifespan=lifespan
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
# ルーターの登録
# =========================================
app.include_router(user_router, prefix="/api")
app.include_router(item_router, prefix="/api")
app.include_router(category_router, prefix="/api")


# =========================================
# ヘルスチェックエンドポイント
# =========================================

@app.get("/", tags=["Root"])
async def root():
    """
    ルートエンドポイント
    APIの基本情報を返す
    """
    return {
        "message": "Welcome to NAFP API (Domain-Driven Design)",
        "version": "2.0.0",
        "docs": "/api/docs",
        "architecture": "DDD (Domain-Driven Design)"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    ヘルスチェックエンドポイント
    アプリケーションの状態を確認
    """
    return {
        "status": "healthy",
        "service": "NAFP API",
        "architecture": "DDD"
    }
