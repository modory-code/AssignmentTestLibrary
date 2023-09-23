from sqlalchemy import Column, Integer, String, CheckConstraint, Enum
from sqlalchemy.orm import validates
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
    isbn = Column(String(13), unique=True, nullable=False)
    page_count = Column(Integer, nullable=False)
    thumbnail_url = Column(String(500))
    # ISBN, PageCount CHECK 제약 조건 설정
    __table_args__ = (
        CheckConstraint('LENGTH(isbn) = 10 OR LENGTH(isbn) = 13'),
        CheckConstraint('page_count > 0', name='positive_integer_check')
    )
    # ISBN, PageCount 스키마 무결성 검사
    @validates('isbn')
    def isbn_length(self, key, value):
        check_length = (10, 13)
        if len(value) not in check_length:
            raise ValueError(f"{key} 컬럼의 길이는 {check_length} 중 하나여야 합니다.")
        if not value:
            raise ValueError(f"{key} 컬럼은 빈 값이 허용되지 않습니다.")
        return value
    @validates('page_count')
    def page_count_positive_integer(self, key, value):
        if value is None:
            raise ValueError(f"{key} 컬럼은 빈 값이 허용되지 않습니다.")
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{key} 컬럼은 양의 정수만 허용됩니다.")
        return value

    # 나머지(thumbnail_url 제외) 스키마 null 무결성 검사
    @validates('title', 'author', 'publication_date')
    def not_null_validate(self, key, value):
        if not value:
            raise ValueError(f"{key} 컬럼은 빈 값이 허용되지 않습니다.")
        return value

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(RoleEnum, nullable=False)

    # 모든 컬럼 스키마 null 무결성 검사
    @validates('username', 'password', 'email', 'role')
    def not_null_validate(self, key, value):
        if not value:
            raise ValueError(f"{key} 컬럼은 빈 값이 허용되지 않습니다.")
        return value