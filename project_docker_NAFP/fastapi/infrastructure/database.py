"""
データベース接続設定
SQLAlchemy非同期エンジンとセッション管理
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator
import os

# 環境変数からデータベース接続情報を取得
DATABASE_USER = os.getenv("POSTGRES_USER", "nafp_user")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpassword")
DATABASE_HOST = os.getenv("POSTGRES_HOST", "postgres")
DATABASE_PORT = os.getenv("POSTGRES_PORT", "5432")
DATABASE_NAME = os.getenv("POSTGRES_DB", "nafp_db")

# PostgreSQL非同期接続URL
DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# 非同期エンジンの作成
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # SQLログを出力（開発環境）
    future=True,
)

# 非同期セッションファクトリーの作成
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# ベースクラス
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    データベースセッション依存性注入用関数
    FastAPIのDependsで使用
    """
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db():
    """データベース初期化（テーブル作成）"""
    async with engine.begin() as conn:
        # 開発環境では既存のテーブルを削除して再作成
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
