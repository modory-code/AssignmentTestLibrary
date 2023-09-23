from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.config import Config

# Database 접속 정보 주소
config = Config('.env')
SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL')

# 커넥션 풀 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 생성
Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 세션 제너레이터
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
