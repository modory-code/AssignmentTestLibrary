from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from routes.book import book_schema, book_crud
from routes.user.user_schema import TokenData
from routes.user.user_router import verify_token

router = APIRouter(
    prefix="/api/book",
)

# 책 목록
@router.get("/list", response_model=book_schema.BookList)
def book_list(
    db: Session = Depends(get_db),
    token_data: TokenData = Depends(verify_token),
    page: int = 0, size: int = 10
):
    # 권한 확인
    if not (token_data.role == "admin" or token_data.role == "user"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="로그인 후 이용 가능합니다.")

    total, _book_list = book_crud.get_book_list(db, skip=page*size, limit=size)
    return {
        'total': total,
        'book_list': _book_list
    }

# 책 정보 조회
@router.get("/detail/", response_model=book_schema.Book)
def book_detail(
    book_title: str | None = None, book_isbn: str | None = None,
    db: Session = Depends(get_db), token_data: TokenData = Depends(verify_token)
):
    # 권한 확인
    if not (token_data.role == "admin" or token_data.role == "user"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="로그인 후 이용 가능합니다.")
    
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
def book_create(
    _book_create: book_schema.BookCreateSchema,
    db: Session = Depends(get_db),
    token_data: TokenData = Depends(verify_token)
):
    if token_data.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="관리자만 책 등록이 가능합니다. 권한을 확인해주십시오."
        )
    book_crud.create_book(db=db, book_create=_book_create)

# 책 수정
@router.put("/update", response_model=book_schema.Book)
def book_update(
    _book_isbn: str,
    _book_update: book_schema.BookUpdateSchema,
    db: Session = Depends(get_db),
    token_data: TokenData = Depends(verify_token)
):
    # ISBN 기준 책 확인
    db_get_book = book_crud.get_book_detail(db, book_isbn=_book_isbn)
    if db_get_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="책을 찾을 수 없습니다."
        )
    # 권한 확인
    if token_data.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="관리자만 책 수정이 가능합니다. 권한을 확인해주십시오."
        )
    # 책 수정
    db_update_book = book_crud.update_book(db, db_book=db_get_book, book_update=_book_update)
    return db_update_book