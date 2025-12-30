"""
SQLAlchemyモデル定義
データベーステーブルとORMマッピング
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index, Boolean
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from datetime import datetime,timezone,timedelta

jst = timezone(timedelta(hours=9), 'JST')

class CategoryModel(Base):
    """カテゴリテーブルモデル"""
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    created_by = Column(String(45), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(jst))
    updated_by = Column(String(45), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(jst), onupdate=datetime.now(jst))
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # リレーションシップ
    items = relationship(
        "ItemModel",
        secondary="item_category",
        back_populates="categories",
        lazy="selectin"
    )