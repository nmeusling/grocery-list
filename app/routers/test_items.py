from app.schemas.item import ItemCreate


def test_create_item(client):
    item = ItemCreate(item="New Item", quantity=2, store="Publix")
    response = client.post("/items/", json=item.model_dump())
    assert response.status_code == 201
    item_id = response.json()["id"]
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["item"] == "New Item"
