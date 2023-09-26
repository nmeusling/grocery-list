from fastapi import APIRouter
from app.groceries import GROCERY_LISTS
from ..schemas.grocery_list import GroceryList, GroceryListCreate
from ..schemas.item import Item, ItemCreate

router = APIRouter()


@router.get("/", status_code=200)
async def root():
    return {"message": "Hello World!"}


@router.get("/lists/{list_name}")
async def read_list(list_name: str):
    for grocery_list in GROCERY_LISTS:
        if grocery_list.name == list_name:
            return grocery_list


@router.post("/lists/", response_model=GroceryList, status_code=201)
async def create_grocery_list(grocery_in: GroceryListCreate):
    items = []
    for item_in in grocery_in.items:
        item = Item(
            id=1, item=item_in.item, quantity=item_in.quantity, store=item_in.store
        )
        items.append(item)
    grocery_list = GroceryList(id=1, name=grocery_in.name, items=items)
    GROCERY_LISTS.append(grocery_list)
    return grocery_list


@router.post("/lists/{list_id}/", response_model=GroceryList, status_code=201)
async def add_item_to_list(list_id: int, item_in: ItemCreate) -> dict:
    grocery_list = [grocery for grocery in GROCERY_LISTS if grocery.id == list_id][0]
    item = Item(id=2, item=item_in.item, quantity=item_in.quantity, store=item_in.store)
    grocery_list.items.append(item)
    GROCERY_LISTS.append(grocery_list)
    return grocery_list
