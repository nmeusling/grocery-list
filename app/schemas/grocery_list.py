from pydantic import BaseModel
from typing import List, Optional
from app.schemas.item import Item, ItemCreate


class GroceryList(BaseModel):
    id: int
    name: str
    items: List[Item]


class GroceryListCreate(BaseModel):
    name: str
    items: Optional[List[ItemCreate]]
