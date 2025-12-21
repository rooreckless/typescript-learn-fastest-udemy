"""
SQLAlchemyモデル定義
データベーステーブルとORMマッピング
"""

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Index, Boolean
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from datetime import datetime


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
