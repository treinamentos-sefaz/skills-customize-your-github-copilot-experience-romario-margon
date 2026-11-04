from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books: list[Book] = []
next_book_id = 1


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # TODO: return all books in the catalog.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: find the requested book or raise HTTPException with status 404.
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput) -> Book:
    # TODO: assign an ID, create the book, store it, and return it.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput) -> Book:
    # TODO: update the requested book or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    # TODO: remove the requested book or raise HTTPException with status 404.
    raise NotImplementedError
