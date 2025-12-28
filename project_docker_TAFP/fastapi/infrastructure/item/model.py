"""
SQLAlchemyモデル定義
データベーステーブルとORMマッピング
"""

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Index, Boolean
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from datetime import datetime


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