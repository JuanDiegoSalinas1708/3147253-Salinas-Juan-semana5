from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from services import product_service
from schemas.product_schema import ProductCreate, ProductResponse
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return product_service.get_products(db)

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)