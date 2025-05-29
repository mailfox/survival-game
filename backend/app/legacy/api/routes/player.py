from fastapi import APIRouter
from app.legacy.models import PlayerBase

router = APIRouter()  # Этот объект должен называться именно router

@router.get("/{player_id}", response_model=PlayerBase)
async def get_player(player_id: int):
    return {
        "name": f"Игрок {player_id}",
        "health": 100,
        "level": 1
    }
