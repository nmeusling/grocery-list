from fastapi import FastAPI
from .routers import lists

app = FastAPI(title="Grocery List API")

app.include_router(lists.router)
