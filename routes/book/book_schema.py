from pydantic import BaseModel, validator

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

    @validator('title')
    def title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('제목은 빈 값이 허용되지 않습니다.')
        return v
    @validator('author')
    def author_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('저자는 빈 값이 허용되지 않습니다.')
        return v
    @validator('publication_date')
    def publication_date_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('출판일은 빈 값이 허용되지 않습니다.')
        return v
    @validator('isbn')
    def isbn_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('ISBN 번호는 빈 값이 허용되지 않습니다.')
        return v
    @validator('page_count')
    def page_count_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('페이지 수는 빈 값이 허용되지 않습니다.')
        return v
    
    @validator('isbn')
    def isbn_length(self, key, value):
        check_length = (10, 13)
        if len(value) not in check_length:
            raise ValueError(f"ISBN 번호의 길이는 {check_length} 중 하나여야 합니다.")
        return value
    
    @validator('page_count')
    def page_count_positive_int(self, key, value):
        if value is None or value <= 0:
            raise ValueError(f"페이지 번호는 양의 정수여야 합니다.")
        return value