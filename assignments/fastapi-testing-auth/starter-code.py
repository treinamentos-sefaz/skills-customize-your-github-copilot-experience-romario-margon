from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import APIKeyHeader
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title="Books API")
API_KEY = "local-dev-key"
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books = [Book(id=1, title="The Little Prince", author="Antoine de Saint-Exupery")]


def require_api_key(api_key: str | None = Depends(api_key_header)) -> str:
    # TODO: reject a missing or incorrect key with HTTP status 401.
    raise NotImplementedError


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return books


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(
    book_input: BookInput,
    api_key: str = Depends(require_api_key),
) -> Book:
    # TODO: create a book with a unique ID, add it to books, and return it.
    raise NotImplementedError


client = TestClient(app)


def test_list_books_returns_books() -> None:
    response = client.get("/books")

    assert response.status_code == status.HTTP_200_OK
    response_books = response.json()
    assert isinstance(response_books, list)
    assert {"id", "title", "author"} <= response_books[0].keys()


# TODO: Add tests for POST /books with valid, missing, and incorrect API keys.
