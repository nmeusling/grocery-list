from pydantic import BaseModel

from typing import Sequence


class Item(BaseModel):
    id: int
    item: str
    quantity: int
    store: str


class ItemSearchResults(BaseModel):
    results: Sequence[Item]


class ItemCreate(BaseModel):
    item: str
    quantity: int
    store: str
    submitter_id: int
