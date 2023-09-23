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
@router.get("/detail/", response_model=list[book_schema.Book])
def book_detail(book_title: str | None = None, book_isbn: str | None = None, db: Session = Depends(get_db)):
    if book_title is None and book_isbn is None:
        # isbn이나 title 모두 들어오지 않은 경우
        raise HTTPException(status_code=400, detail="책 제목이나 ISBN 번호 둘 중 하나는 필수로 입력해야 합니다.")
    else:
        if book_title:
            book = book_crud.get_book_detail(db, book_title=book_title)
        if book_isbn:
            book = book_crud.get_book_detail(db, book_isbn=book_isbn)
    if book is None:
        raise HTTPException(status_code=404, detail="책을 찾을 수 없습니다.")
    return book

# 책 등록
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def book_create(_book_create: book_schema.BookCreateSchema,
                db: Session = Depends(get_db)):
    book_crud.create_book(db=db, book_create=_book_create)