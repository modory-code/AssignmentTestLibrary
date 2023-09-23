from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models import User
from routes.user.user_schema import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"])

# 회원 가입
def create_user(db: Session, user_create: UserCreate):
    db_create_user = User(
        username=user_create.username,
        password=pwd_context.hash(user_create.password1),
        email=user_create.email,
        role=user_create.model_dump()['role']
    )
    db.add(db_create_user)
    db.commit()