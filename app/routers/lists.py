from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.grocery_list import GroceryList, GroceryListCreate
from app.schemas.item import ItemCreate
from app.db import crud
from app.db.session import get_db

router = APIRouter()


@router.get("/lists/", response_model=list[GroceryList])
async def read_grocery_lists(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """
    Get all grocery lists
    """
    return crud.get_grocery_lists(db, skip, limit)


@router.get("/lists/{list_id}", response_model=GroceryList)
async def read_grocery_list(list_id: int, db: Session = Depends(get_db)):
    """
    Get grocery list by id
    """
    grocery_list = crud.get_grocery_list(db, grocery_list_id=list_id)
    if grocery_list is None:
        raise HTTPException(
            status_code=404, detail=f"Grocery list with id {list_id} not found"
        )
    return grocery_list


@router.post("/lists/", response_model=GroceryList, status_code=201)
async def create_grocery_list(
    grocery_in: GroceryListCreate, db: Session = Depends(get_db)
):
    """
    Create a new grocery list
    """
    return crud.create_grocery_list(db, grocery_list=grocery_in)


@router.post("/lists/{list_id}/", response_model=GroceryList, status_code=201)
async def create_grocery_list_item(
    list_id: int, item_in: ItemCreate, db: Session = Depends(get_db)
):
    """
    Add an item to an existing grocery list
    """
    db_list = crud.get_grocery_list(db, list_id)
    if not db_list:
        raise HTTPException(
            status_code=404, detail=f"Grocery list with id {list_id} not found"
        )
    crud.create_grocery_list_item(db, list_id, item_in)
    return db_list
