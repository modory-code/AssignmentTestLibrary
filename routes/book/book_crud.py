from sqlalchemy.orm import Session

from models import Book
from routes.book.book_schema import BookCreateSchema, BookUpdateSchema

# 책 목록 페이지 별 불러오기
def get_book_list(db: Session, skip: int = 0, limit: int = 0):
    _book_list = db.query(Book)\
        .order_by(Book.id.desc())\
        
    total = _book_list.count()
    book_list = _book_list.offset(skip).limit(limit).all()
    
    return total, book_list

# 책 정보 상세 조회
def get_book_detail(db: Session, book_title: str | None = None, book_isbn: str | None = None):
    if book_title:
        book_detail = db.query(Book).filter(Book.title == book_title).first()
    if book_isbn:
        book_detail = db.query(Book).filter(Book.isbn == book_isbn).first()
    if book_detail is None:
        return None
    return book_detail

# 책 등록
def create_book(db: Session, book_create: BookCreateSchema):
    db_create_book = Book(
        title = book_create.title,
        author = book_create.author,
        publication_date = book_create.publication_date,
        isbn = book_create.isbn,
        page_count = book_create.page_count,
        thumbnail_url = book_create.thumbnail_url
    )
    db.add(db_create_book)
    db.commit()

# 책 수정
def update_book(db: Session, db_book: Book, book_update: BookUpdateSchema):
    print('db_book', db_book.title)
    print('book_update', book_update.title)
    db_book.title = book_update.title
    db_book.author = book_update.author
    db_book.publication_date = book_update.publication_date
    db_book.isbn = book_update.isbn
    db_book.page_count = book_update.page_count
    db_book.thumbnail_url = book_update.thumbnail_url
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# 책 삭제
def delete_book(db: Session, book_isbn_list: list[str]):
    # 삭제 시점 책 isbn 유효성 확인
    valid_isbn_list = []
    for isbn in book_isbn_list:
        book = db.query(Book).filter(Book.isbn == isbn).first()
        if book:
            valid_isbn_list.append(book)
    # 유효성 통과한 책들 삭제
    db.query(Book).filter(Book.isbn.in_(valid_isbn_list)).delete(synchronize_session=False)
    db.commit()