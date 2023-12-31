import pytest

from app.schemas.grocery_list import GroceryListCreate
from app.schemas.item import ItemCreate

# SQLALCHEMY_DATABASE_URL = "sqlite://"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     poolclass=StaticPool,
# )

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=Flase, bind=engine)
# Base.metadata.create_all(bind=engine)


# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()


# app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def grocery_list(client):
    grocery_list = GroceryListCreate(name="Test Grocery List", items=[])
    response = client.post("/lists/", json=grocery_list.model_dump())
    return response.json()["id"]


@pytest.fixture
def item():
    yield ItemCreate(item="New Item", quantity=4, store="Store")


def test_create_grocery_list_no_items(client):
    grocery_list_name = "New Grocery List"
    grocery_list = GroceryListCreate(name=grocery_list_name, items=[])
    response = client.post("/lists/", json=grocery_list.model_dump())
    assert response.status_code == 201
    assert response.json()["name"] == grocery_list_name
    assert len(response.json()["items"]) == 0


def test_get_grocery_list(client, grocery_list: int):
    response = client.get(f"/lists/{grocery_list}")
    assert response.status_code == 200
    assert len(response.json()["items"]) == 0


def test_get_grocery_lists(client, grocery_list):
    response = client.get("/lists/")
    assert response.status_code == 200
    assert len(response.json()) > 1


def test_add_item_to_list(client, grocery_list, item):
    response = client.post(f"/lists/{grocery_list}/", json=item.model_dump())
    assert response.status_code == 201
    assert len(response.json()["items"]) == 1


def test_add_item_to_list_non_existant_list(client, grocery_list, item):
    grocery_lists = len(client.get("/lists/").json())
    response = client.post(f"/lists/{grocery_lists+1}/", json=item.model_dump())
    assert response.status_code == 404
