"""
認証・認可ヘルパー関数
JWT トークンの生成と検証
"""

from datetime import datetime, timedelta,timezone
from typing import Optional
from jose import JWTError, jwt
import bcrypt

# JWT設定
SECRET_KEY = "your-secret-key-change-this-in-production"  # 本番環境では環境変数から取得すべき
ALGORITHM = "HS256"
# JWTトークンの有効期限（分）
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
ACCESS_TOKEN_EXPIRE_MINUTES = 3000
jst = timezone(timedelta(hours=9))

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


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    JWTアクセストークンを生成
    
    Args:
        data: トークンに含めるデータ
        expires_delta: トークンの有効期限（デフォルト: 30分）
        
    Returns:
        JWTトークン文字列
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(tz=jst) + expires_delta
    else:
        expire = datetime.now(tz=jst) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    JWTトークンをデコード
    
    Args:
        token: JWTトークン文字列
        
    Returns:
        デコードされたペイロード、エラーの場合None
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
