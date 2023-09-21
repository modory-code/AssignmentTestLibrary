from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database 접속 정보 주소
SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://modory:moco1!@127.0.0.1:3306/library"

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
