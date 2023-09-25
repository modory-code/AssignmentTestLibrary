from pydantic import BaseModel, validator
from typing import List

class Book(BaseModel):
    id: int
    title: str
    author: str
    publication_date: str
    isbn: str
    page_count: int
    thumbnail_url: str

    class Config:
        orm_mode = True

class BookCreateSchema(BaseModel):
    title: str
    author: str
    publication_date: str
    isbn: str
    page_count: int
    thumbnail_url: str | None = None

    # 유효성 검사
    @validator('title', 'author', 'publication_date', 'isbn')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    @validator('isbn')
    def isbn_length(cls, v):
        check_length = (10, 13)
        if len(v) not in check_length:
            raise ValueError(f"ISBN 번호의 길이는 {check_length} 중 하나여야 합니다.")
        return v
    @validator('page_count')
    def page_count_not_empty_positive_int(cls, v):
        if not v:
            raise ValueError('페이지 수는 빈 값이 허용되지 않습니다.')
        if not isinstance(v, int) or v <= 0:
            raise ValueError('페이지 수는 양의 정수만 허용됩니다.')
        return v
    
class BookList(BaseModel):
    total: int = 0
    book_list: list[Book] = []

class BookUpdateSchema(BookCreateSchema):
    id: int

class BookDeleteSchema(BaseModel):
    isbn: List[str]