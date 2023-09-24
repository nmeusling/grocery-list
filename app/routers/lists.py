from fastapi import APIRouter

router = APIRouter()


@router.get("/", status_code=200)
async def root():
    return {"message": "Hello World!"}


@router.get("/lists/{list_name}")
async def read_list(list_name: str):
    return {"message": list_name}
