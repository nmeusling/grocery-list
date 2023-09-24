from fastapi import FastAPI
from .routers import lists, items

app = FastAPI(title="Grocery List API")

app.include_router(lists.router)
app.include_router(items.router)
