from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class GroceryList(Base):
    __tablename__ = "grocery_lists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    items = relationship("GroceryItem", back_populates="grocery_list")
