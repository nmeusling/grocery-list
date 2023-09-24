from fastapi import APIRouter
from ..groceries import GROCERY_LIST

router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    result = [item for item in GROCERY_LIST if item["id"] == item_id]
    if result:
        return result[0]
