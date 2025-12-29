"""
ユーザーリポジトリ実装
"""

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime,timezone,timedelta

from domain import UserEntity,AbstractUserRepository
from .model import UserModel

jst = timezone(timedelta(hours=+9), 'JST')

class UserRepository(AbstractUserRepository):
    """ユーザーリポジトリ実装クラス"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: UserEntity) -> UserEntity:
        """ユーザーを作成"""
        db_user = UserModel(
            name=user.name.value,
            password_hash=user.password_hash.value,
            email=user.email.value,
            created_at=datetime.now(tz=jst),
            created_by=user.created_by.value,
            updated_by=user.updated_by.value,
            updated_at=datetime.now(tz=jst)
        )
        self.session.add(db_user)
        await self.session.flush()
        # await self.session.refresh(db_user)
        await self.session.commit()
        return UserEntity.model_validate(db_user, from_attributes=True)

    async def find_by_id(self, user_id: int) -> Optional[UserEntity]:
        """IDでユーザーを検索"""
        result = await self.session.execute(
            select(UserModel).where(
                UserModel.id == user_id,
                UserModel.deleted_at.is_(None)
            )
        )
        db_user = result.scalar_one_or_none()
        return UserEntity.model_validate(db_user, from_attributes=True) if db_user else None

    async def find_by_email(self, email: str) -> Optional[UserEntity]:
        """メールアドレスでユーザーを検索"""
        result = await self.session.execute(
            select(UserModel).where(
                UserModel.email == email,
                UserModel.deleted_at.is_(None)
            )
        )
        db_user = result.scalar_one_or_none()
        return UserEntity.model_validate(db_user, from_attributes=True) if db_user else None

    async def find_all(self, skip: int = 0, limit: int = 100) -> List[UserEntity]:
        """全ユーザーを取得"""
        result = await self.session.execute(
            select(UserModel)
            .where(UserModel.deleted_at.is_(None))
            .offset(skip)
            .limit(limit)
        )
        db_users = result.scalars().all()
        return [UserEntity.model_validate(user, from_attributes=True) for user in db_users]

    async def update(self, user_id: int, user: UserEntity) -> Optional[UserEntity]:
        """ユーザーを更新"""
        result = await self.session.execute(
            select(UserModel).where(
                UserModel.id == user_id,
                UserModel.deleted_at.is_(None)
            )
        )
        db_user = result.scalar_one_or_none()
        
        if not db_user:
            return None

        db_user.name = user.name.value
        db_user.email = user.email.value
        if user.password_hash:
            db_user.password_hash = user.password_hash.value
        db_user.updated_by = user.updated_by.value
        db_user.updated_at = datetime.now(tz=jst)

        await self.session.flush()
        # await self.session.refresh(db_user)
        await self.session.commit()
        return UserEntity.model_validate(db_user, from_attributes=True)

    async def delete(self, user_id: int, updated_by: str) -> bool:
        """ユーザーを論理削除
        
        Args:
            user_id: ユーザーID
            updated_by: 更新者
            
        Returns:
            削除が成功した場合True
        """
        result = await self.session.execute(
            select(UserModel).where(
                UserModel.id == user_id,
                UserModel.deleted_at.is_(None)
            )
        )
        db_user = result.scalar_one_or_none()
        
        if not db_user:
            return False

        db_user.updated_by = updated_by
        db_user.updated_at = datetime.now(tz=jst)
        db_user.deleted_at = datetime.now(tz=jst)
        await self.session.flush()
        await self.session.commit()
        return True
