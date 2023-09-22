from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from routes.book import book_schema, book_crud

router = APIRouter(
    prefix="/api/book",
)

@router.get("/list", response_model=list[book_schema.Book])
def book_list(db: Session = Depends(get_db)):
    _book_list = book_crud.get_book_list(db)
    return _book_list

@router.get("/detail/{book_isbn}", response_model=book_schema.Book)
def book_detail(book_isbn: str, db: Session = Depends(get_db)):
    book = book_crud.get_book_detail(db, book_isbn=book_isbn)
    return book