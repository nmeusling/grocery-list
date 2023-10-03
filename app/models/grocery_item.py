from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class GroceryItem(Base):
    __tablename__ = "grocery_items"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String(256), nullable=False)
    quantity = Column(Integer, nullable=True)
    store = Column(String(256), nullable=True)
    grocery_list_id = Column(Integer, ForeignKey("grocery_lists.id"), nullable=True)
    grocery_list = relationship("GroceryList", back_populates="items")
