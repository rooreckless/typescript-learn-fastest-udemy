"""
ユーザーユースケース（アプリケーションサービス）
ビジネスロジックの実行とトランザクション管理
"""

from typing import List, Optional
import bcrypt

from domain import UserEntity,AbstractUserRepository


class UserService:
    """ユーザーサービスクラス"""

    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    @staticmethod
    def hash_password(password: str) -> str:
        """
        パスワードをハッシュ化（bcryptを使用）
        
        Args:
            password: 平文パスワード
            
        Returns:
            bcryptハッシュ（文字列）
        """
        # パスワードをバイト列に変換してハッシュ化
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        # ハッシュを文字列として返す
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        パスワードを検証
        
        Args:
            plain_password: 平文パスワード
            hashed_password: ハッシュ化されたパスワード
            
        Returns:
            パスワードが一致する場合True
        """
        password_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)

    async def create_user(
        self,
        name: str,
        email: str,
        password: str,
        created_by: str,
        admin: bool = False
    ) -> UserEntity:
        """
        新しいユーザーを作成
        
        Args:
            name: ユーザー名
            email: メールアドレス
            password: パスワード（平文）
            created_by: 作成者
            admin: 管理者フラグ
            
        Returns:
            作成されたユーザーエンティティ
            
        Raises:
            ValueError: メールアドレスが既に使用されている場合
        """
        # メールアドレスの重複チェック
        existing_user = await self.user_repository.find_by_email(email)
        if existing_user:
            raise ValueError(f"Email {email} is already registered")

        # パスワードをハッシュ化
        password_hash = self.hash_password(password)

        # ユーザーエンティティを作成
        user = UserEntity(
            name=name,
            email=email,
            password_hash=password_hash,
            admin=admin,
            created_by=created_by,
            updated_by=created_by
        )

        return await self.user_repository.create(user)

    async def get_user_by_id(self, user_id: int) -> Optional[UserEntity]:
        """IDでユーザーを取得"""
        return await self.user_repository.find_by_id(user_id)

    async def get_user_by_email(self, email: str) -> Optional[UserEntity]:
        """メールアドレスでユーザーを取得"""
        return await self.user_repository.find_by_email(email)

    async def get_all_users(self, skip: int = 0, limit: int = 100) -> List[UserEntity]:
        """全ユーザーを取得"""
        return await self.user_repository.find_all(skip, limit)

    async def update_user(
        self,
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        admin: Optional[bool] = None,
        updated_by: str = "system"
    ) -> Optional[UserEntity]:
        """
        ユーザー情報を更新
        
        Args:
            user_id: ユーザーID
            name: 新しいユーザー名（オプション）
            email: 新しいメールアドレス（オプション）
            password: 新しいパスワード（オプション）
            admin: 管理者フラグ（オプション）
            updated_by: 更新者
            
        Returns:
            更新されたユーザーエンティティ
            
        Raises:
            ValueError: メールアドレスが既に使用されている場合
        """
        # 既存ユーザーを取得
        existing_user = await self.user_repository.find_by_id(user_id)
        if not existing_user:
            return None

        # メールアドレスの重複チェック
        if email and email != existing_user.email.value:
            duplicate_user = await self.user_repository.find_by_email(email)
            if duplicate_user:
                raise ValueError(f"Email {email} is already registered")

        # 更新内容を反映
        updated_user = UserEntity(
            id=user_id,
            name=name if name else existing_user.name,
            email=email if email else existing_user.email,
            password_hash=self.hash_password(password) if password else existing_user.password_hash,
            admin=admin if admin is not None else existing_user.admin,
            created_by=existing_user.created_by,
            created_at=existing_user.created_at,
            updated_by=updated_by
        )

        return await self.user_repository.update(user_id, updated_user)

    async def delete_user(self, user_id: int) -> bool:
        """ユーザーを論理削除"""
        return await self.user_repository.delete(user_id)

    async def authenticate_user(self, email: str, password: str) -> Optional[UserEntity]:
        """
        ユーザー認証
        
        Args:
            email: メールアドレス
            password: パスワード
            
        Returns:
            認証成功時はユーザーエンティティ、失敗時はNone
        """
        user = await self.user_repository.find_by_email(email)
        if not user:
            return None

        if not self.verify_password(password, user.password_hash.value):
            return None

        return user
