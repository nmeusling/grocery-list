from app.schemas.item import ItemCreate


def test_get_item(client):
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "item": "Milk",
        "quantity": 2,
        "store": "Publix",
    }


def test_search_items_max_result(client):
    max_results = 1
    response = client.get(f"/items/search/?max_results={max_results}")
    assert response.status_code == 200
    assert len(response.json()["results"]) == max_results


def test_search_items_invalid_keyword(client):
    keyword = "there are no matching items with this keyword"
    response = client.get(f"/items/search/?keyword={keyword}")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 0


def test_search_items_valid_keyword(client):
    keyword = "cake"
    response = client.get(f"/items/search/?keyword={keyword}")
    assert response.status_code == 200
    assert len(response.json()["results"]) >= 2
    assert {
        "id": 5,
        "item": "Cup cake",
        "quantity": 2,
        "store": "Costco",
    } in response.json()["results"]
    assert {
        "id": 4,
        "item": "Cake",
        "quantity": 2,
        "store": "Costco",
    } in response.json()["results"]


def test_create_item(client):
    item = ItemCreate(item="New Item", quantity=2, store="Publix", submitter_id=2)
    response = client.post("/item/", json=item.model_dump())
    assert response.status_code == 201
