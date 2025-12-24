"""
認証APIエンドポイント
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from infrastructure.database import provide_db
from presentation.dependencies import provide_user_service
from ..schemas import LoginRequest, LoginResponse
from ..schemas import UserResponse
from presentation.auth import create_access_token, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=LoginResponse,
    summary="ログイン"
)
async def login(
    request: LoginRequest,
    db: AsyncSession = Depends(provide_db)
):
    """
    ユーザー認証を行い、JWTトークンを発行します
    
    - **email**: メールアドレス
    - **password**: パスワード
    
    成功時にはアクセストークンとユーザー情報を返します
    """
    from application.use_cases.auth.login import LoginUseCase
    service = provide_user_service(db)
    use_case = LoginUseCase(service)
    result = await use_case(request)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token, user = result
    
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.model_validate(user)
    )
