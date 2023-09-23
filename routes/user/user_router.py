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
    user_crud.create_user(db=db, user_create=_user_create)