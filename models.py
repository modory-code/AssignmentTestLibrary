from sqlalchemy import Column, Integer, String, CheckConstraint, Enum
from database import Base

# 권한 Enum
RoleEnum = Enum('user', 'admin')

# 테이블 구조 정의
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    publication_date = Column(String(10), nullable=False)
    isbn = Column(String(13), nullable=False)
    page_count = Column(Integer, nullable=False)
    thumbnail_url = Column(String(500))
    # ISBN CHECK 제약 조건 설정
    __table_args__ = (
        CheckConstraint('LENGTH(isbn) = 10 OR LENGTH(isbn) = 13'),
    )

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    role = Column(RoleEnum, nullable=False)

