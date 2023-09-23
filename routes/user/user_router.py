from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from routes.user import user_schema, user_crud

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