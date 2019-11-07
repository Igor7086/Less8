import pytest
from module_CRUD import CRUD

body_positive = {"title": "Iliad", "author": "Homer"}
body_updated_book = {"title": "Iliad and Odyssey", "author": "Homer"}


@pytest.fixture()
def setup():
    operations = CRUD()
    book_response = operations.create_book(body_positive)
    book = book_response.json()
    book["status_code"] = book_response.status_code
    print(book)
    yield book
    operations.delete_book(body_positive)


def test_check_that_book_was_created(setup):
    for i in body_positive:
        assert setup[i] == body_positive[i]


def test_check_that_changing_data_with_existing_id_is_ok(setup):
    operations = CRUD()
    updated_book_response = operations.update_book(setup["id"], body_updated_book)
    updated_book = updated_book_response.json()
    print(updated_book)
    assert setup["id"] == updated_book["id"]


def test_deleted_book(setup):
    operations = CRUD()
    deleted_book_response = operations.delete_book(setup["id"])
    print(deleted_book_response, "No Content")
    assert 204 == deleted_book_response.status_code

