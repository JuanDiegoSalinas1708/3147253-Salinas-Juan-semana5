from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from services import book_service
from schemas.book_schema import BookCreate, BookResponse
from typing import List

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[BookResponse])
def list_books(db: Session = Depends(get_db)):
    return book_service.get_books(db)

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book)
