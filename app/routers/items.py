from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.item import Item, ItemCreate
from app.db import crud
from app.db.session import get_db


router = APIRouter()


@router.get("/items/{item_id}", response_model=Item, status_code=200)
async def read_grocery_item(item_id: int, db: Session = Depends(get_db)) -> dict:
    grocery_item = crud.get_grocery_item(db, grocery_item_id=item_id)
    if grocery_item is None:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")
    return grocery_item


@router.post("/items/", response_model=Item, status_code=201)
async def create_grocery_item(
    grocery_item_in: ItemCreate, db: Session = Depends(get_db)
):
    """
    Create a new grocery item
    """
    return crud.create_grocery_item(db, grocery_item=grocery_item_in)
