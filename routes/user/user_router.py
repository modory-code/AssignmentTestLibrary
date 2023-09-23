from datetime import timedelta, datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status
from starlette.config import Config

from database import get_db
from routes.user import user_schema, user_crud
from routes.user.user_crud import pwd_context

config = Config('.env')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = "HS256"

# SECRET_KEY = 

router = APIRouter(
    prefix="/api/user"
)

# 회원 가입
@router.post("/join", status_code=status.HTTP_204_NO_CONTENT)
def user_join(_user_create: user_schema.UserCreate,
              db: Session = Depends(get_db)):
    existing_user = user_crud.get_existing_user(db=db, user_create=_user_create)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    user_crud.create_user(db=db, user_create=_user_create)

# 로그인
@router.post("/login", response_model=user_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    # 유저와 암호 확인
    user = user_crud.get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="아이디 혹은 비밀번호가 일치하지 않습니다.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # 액세스 토큰 생성
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }