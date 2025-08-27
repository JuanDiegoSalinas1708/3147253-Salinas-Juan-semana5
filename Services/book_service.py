from sqlalchemy.orm import Session
from models.book import Book
from schemas.book_schema import BookCreate

def get_books(db: Session):
    return db.query(Book).all()

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
