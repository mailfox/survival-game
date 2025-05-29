from typing import List
from fastapi import APIRouter
from app.legacy.models import InventoryItem

router = APIRouter(prefix="/inventory", tags=["inventory"])

fake_db = [
    {"id": 1, "name": "Меч", "type": "weapon", "quantity": 1},
    {"id": 2, "name": "Яблоко", "type": "food", "quantity": 3}
]

@router.get("/{player_id}", response_model=List[InventoryItem])
async def get_inventory(player_id: int):
    return fake_db
