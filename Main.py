from fastapi import FastAPI
from routers import products, books
from database.connection import Base, engine

# Crear tablas en la BD
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Semana 5 - FastAPI con SQLite")

# Incluir routers
app.include_router(products.router)
app.include_router(books.router)

@app.get("/")
def root():
    return {"message": "API Semana 5 funcionando 🚀"}
