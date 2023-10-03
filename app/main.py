from fastapi import FastAPI
from app.routers import lists, items
from app.db.base_class import Base
from app.db.session import engine


Base.metadata.create_all(bind=engine)
app = FastAPI(title="Grocery List API")


app.include_router(lists.router)
app.include_router(items.router)
