from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

app = FastAPI()

libros = []

@app.post("/books/")
def create_book(book: Book):
    libros.append(book)
    return book

@app.get("/books/")
def get_books():
    return libros

@app.get("/books/{id}")
def get_book(id: int):
    libro = None
    for b in libros:
        if b.id == id:
            libro = b
    
    if libro != None:
        return libro
    return {"error": "Book not found"}
 

@app.put("/books/{id}")
def update_book(id: int, book: Book):
    libro = None
    for b in libros:
        if b.id == id:
            libro = b
    
    if libro == None:
        return {"error": "Book not found"}
    index = libros.index(libro)
    book.id = id 
    libros[index] = book
    return book

@app.delete("/books/{id}")
def delete_book(id: int):
    libro = None
    for b in libros:
        if b.id == id:
            libro = b
    
    if libro == None:
        return {"error": "Book not found"}
    
    libros.remove(libro)
    return libro