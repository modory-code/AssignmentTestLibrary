from models import Book
from sqlalchemy.orm import Session

def get_book_list(db: Session):
    book_list = db.query(Book)\
        .order_by(Book.id.desc())\
        .all()
    return book_list

def get_book_detail(db: Session, book_isbn: str):
    book_detail = db.query(Book).get(book_isbn)
    return book_detail