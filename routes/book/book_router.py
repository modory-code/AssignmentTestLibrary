from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from routes.book import book_schema, book_crud

router = APIRouter(
    prefix="/api/book",
)

# 책 목록
@router.get("/list", response_model=list[book_schema.Book])
def book_list(db: Session = Depends(get_db)):
    _book_list = book_crud.get_book_list(db)
    return _book_list

# 책 정보 조회
@router.get("/detail/{book_isbn}", response_model=list[book_schema.Book])
def book_detail(book_isbn: str, db: Session = Depends(get_db)):
    book = book_crud.get_book_detail(db, book_isbn=book_isbn)
    if book is None:
        raise HTTPException(status_code=404, detail="책을 찾을 수 없습니다.")
    return book

# 책 등록
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def book_create(_book_create: book_schema.BookCreateSchema,
                db: Session = Depends(get_db)):
    book_crud.create_book(db=db, book_create=_book_create)