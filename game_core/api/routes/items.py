from fastapi import APIRouter
from game_core.models import ItemCreate

router = APIRouter()

@router.post("/")
async def create_item(item: ItemCreate):
    return {"status": "created", "item": item}
