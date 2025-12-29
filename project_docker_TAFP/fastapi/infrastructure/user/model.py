"""
SQLAlchemyモデル定義
データベーステーブルとORMマッピング
"""

from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, ForeignKey, Index, Boolean
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from datetime import datetime,timezone,timedelta

jst = timezone(timedelta(hours=9), 'JST')

class UserModel(Base):
    """ユーザーテーブルモデル"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    admin = Column(Boolean, nullable=False, default=False)
    created_by = Column(String(45), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    updated_by = Column(String(45), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    deleted_at = Column(DateTime(timezone=True), nullable=True)
