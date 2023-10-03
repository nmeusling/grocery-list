from pydantic import BaseModel, ConfigDict
from typing import List
from app.schemas.item import Item


class GroceryListBase(BaseModel):
    name: str


class GroceryListCreate(GroceryListBase):
    pass


class GroceryList(GroceryListBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    items: List[Item]
