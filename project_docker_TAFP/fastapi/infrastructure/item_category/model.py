"""
SQLAlchemyモデル定義
データベーステーブルとORMマッピング
"""

from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime, ForeignKey, Index, Boolean
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from datetime import datetime,timezone,timedelta

jst = timezone(timedelta(hours=9), 'JST')

class ItemCategoryModel(Base):
    """商品カテゴリ関連テーブルモデル"""
    __tablename__ = "item_category"

    item_id = Column(Integer, ForeignKey("items.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    created_by = Column(String(45), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    updated_by = Column(String(45), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    # インデックス
    __table_args__ = (
        Index("idx_item_category_category_id", "category_id"),
    )
