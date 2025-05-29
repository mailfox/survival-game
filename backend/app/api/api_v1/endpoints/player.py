from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud import crud_player
from app.schemas.player import PlayerBase, PlayerAction

router = APIRouter()

@router.post("/eat", response_model=PlayerBase)
def eat(
    player_action: PlayerAction,
    db: Session = Depends(get_db)
):
    player = crud_player.get_player(db, player_action.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    player.hunger = min(player.hunger + 30, 100)
    db.commit()
    db.refresh(player)
    return player