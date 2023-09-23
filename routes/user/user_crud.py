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

# 회원 가입 전 충돌 확인
def get_existing_user(db: Session, user_create: UserCreate):
    check_user = db.query(User).\
        filter(
            (User.username==user_create.username) |
            (User.email==user_create.email)
        ).first()
    return check_user

# 로그인
def get_user(db: Session, username: str):
    return db.query(User).filter(User.username==username).first()