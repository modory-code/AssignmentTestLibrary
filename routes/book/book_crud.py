from sqlalchemy.orm import Session

from models import Book
from routes.book.book_schema import BookCreateSchema

def get_book_list(db: Session):
    book_list = db.query(Book)\
        .order_by(Book.id.desc())\
        .all()
    return book_list

def get_book_detail(db: Session, book_title: str | None = None, book_isbn: str | None = None):
    if book_title:
        book_detail = db.query(Book).filter(Book.title == book_title).first()
    if book_isbn:
        book_detail = db.query(Book).filter(Book.isbn == book_isbn).first()
    if book_detail is None:
        return None
    return [book_detail]

def create_book(db: Session, book_create: BookCreateSchema):
    db_create_book = Book(
        title=book_create.title,
        author=book_create.author,
        publication_date=book_create.publication_date,
        isbn=book_create.isbn,
        page_count=book_create.page_count,
        thumbnail_url=book_create.thumbnail_url
    )
    db.add(db_create_book)
    db.commit()