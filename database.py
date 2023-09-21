from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database 접속 정보 주소
SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:siryu33@127.0.0.1:3306/library"

# 커넥션 풀 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

# 세션 생성
Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
session = Session()

# 권한 Enum
RoleEnum = Enum('user', 'admin')

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(String)
    isbn = Column(String(13))
    page_count = Column(Integer)
    thumbnail_url = Column(String)
    # ISBN CHECK 제약 조건 설정
    __table_args__ = (
        CheckConstraint('LENGTH(isbn) = 10 OR LENGTH(isbn) = 13'),
    )

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    role = Column(RoleEnum)

# 테이블 생성 및 갱신
Base.metadata.create_all(engine)