"""
SQLAlchemyモデル定義
データベーステーブルとORMマッピング
"""

from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, ForeignKey, Index, Boolean
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from datetime import datetime,timezone,timedelta

jst = timezone(timedelta(hours=9), 'JST')

class ItemModel(Base):
    """商品テーブルモデル"""
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(Integer, nullable=False)
    created_by = Column(String(45), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    updated_by = Column(String(45), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # リレーションシップ
    categories = relationship(
        "CategoryModel",
        secondary="item_category",
        back_populates="items",
        lazy="selectin"
    )