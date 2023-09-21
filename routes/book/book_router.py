from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from routes.book import book_schema
from models import Book

router = APIRouter(
    prefix="/api/book",
)

@router.get("/list", response_model=list[book_schema.Book])
def book_list(db: Session = Depends(get_db)):
    _book_list = db.query(Book).order_by(Book.id.desc()).all()
    return _book_list
