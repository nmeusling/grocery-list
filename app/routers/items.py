from typing import Optional

from fastapi import APIRouter, Query
from ..groceries import GROCERY_LIST
from ..schemas.item import Item, ItemSearchResults, ItemCreate

router = APIRouter()


@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int) -> dict:
    result = [item for item in GROCERY_LIST if item["id"] == item_id]
    if result:
        return result[0]


@router.get("/items/search/", response_model=ItemSearchResults)
async def search_items(
    keyword: Optional[str] = Query(None, min_length=3, example="eggs"),
    max_results: Optional[int] = 10,
) -> dict:
    if not keyword:
        return {"results": GROCERY_LIST[:max_results]}

    results = list(
        filter(lambda item: keyword.lower() in item["item"].lower(), GROCERY_LIST)
    )
    return {"results": results[:max_results]}


@router.post("/item/", status_code=201, response_model=Item)
async def create_item(item_in: ItemCreate) -> dict:
    """
    Create a new recipe (in memory only)
    """
    new_entry_id = len(GROCERY_LIST) + 1
    item_entry = Item(
        id=new_entry_id,
        item=item_in.item,
        quantity=item_in.quantity,
        store=item_in.store,
    )
    GROCERY_LIST.append(item_entry.dict())
    return item_entry
