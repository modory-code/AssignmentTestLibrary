from pydantic import BaseModel

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