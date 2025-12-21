"""
SQLAlchemyモデル定義
データベーステーブルとORMマッピング
"""

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Index, Boolean
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from datetime import datetime


class UserModel(Base):
    """ユーザーテーブルモデル"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    admin = Column(Boolean, nullable=False, default=False)
    created_by = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    updated_by = Column(String(45), nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(TIMESTAMP, nullable=True)


class ItemModel(Base):
    """商品テーブルモデル"""
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(Integer, nullable=False)
    created_by = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    updated_by = Column(String(45), nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(TIMESTAMP, nullable=True)

    # リレーションシップ
    categories = relationship(
        "CategoryModel",
        secondary="item_category",
        back_populates="items",
        lazy="selectin"
    )


class CategoryModel(Base):
    """カテゴリテーブルモデル"""
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    created_by = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    updated_by = Column(String(45), nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(TIMESTAMP, nullable=True)

    # リレーションシップ
    items = relationship(
        "ItemModel",
        secondary="item_category",
        back_populates="categories",
        lazy="selectin"
    )


class ItemCategoryModel(Base):
    """商品カテゴリ関連テーブルモデル"""
    __tablename__ = "item_category"

    item_id = Column(Integer, ForeignKey("items.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    created_by = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    updated_by = Column(String(45), nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(TIMESTAMP, nullable=True)

    # インデックス
    __table_args__ = (
        Index("idx_item_category_category_id", "category_id"),
    )
