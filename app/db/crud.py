from sqlalchemy.orm import Session

from app.models.grocery_list import GroceryList
from app.models.grocery_item import GroceryItem
from app import schemas


def get_grocery_list(db: Session, grocery_list_id: int):
    return db.query(GroceryList).filter(GroceryList.id == grocery_list_id).first()


def get_grocery_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GroceryList).offset(skip).limit(limit).all()


def create_grocery_list(db: Session, grocery_list: schemas.grocery_list.GroceryList):
    db_grocery_list = GroceryList(name=grocery_list.name)
    db.add(db_grocery_list)
    db.commit()
    db.refresh(db_grocery_list)
    return db_grocery_list


def get_grocery_item(db: Session, grocery_item_id: int):
    return db.query(GroceryItem).filter(GroceryItem.id == grocery_item_id).first()


def get_grocery_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GroceryItem).offset(skip).limit(limit).all()


def create_grocery_item(db: Session, grocery_item: schemas.item.Item):
    db_grocery_item = GroceryItem(
        item=grocery_item.item, quantity=grocery_item.quantity, store=grocery_item.store
    )
    db.add(db_grocery_item)
    db.commit()
    db.refresh(db_grocery_item)
    return db_grocery_item


def create_grocery_list_item(db: Session, list_id: int, item_in: schemas.item.Item):
    db_item = GroceryItem(
        item=item_in.item,
        quantity=item_in.quantity,
        store=item_in.store,
        grocery_list_id=list_id,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
