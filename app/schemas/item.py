from pydantic import BaseModel

from typing import Sequence, Optional


class ItemBase(BaseModel):
    item: str
    quantity: Optional[int]
    store: Optional[str]


class Item(ItemBase):
    id: int


class ItemSearchResults(BaseModel):
    results: Sequence[Item]


class ItemCreate(ItemBase):
    pass
