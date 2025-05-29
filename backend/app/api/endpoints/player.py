from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from models.player import Player
from schemas.player import PlayerBase, PlayerUpdate

router = APIRouter()

@router.get("/{player_id}", response_model=PlayerBase)
def read_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.patch("/{player_id}", response_model=PlayerBase)
def update_player_endpoint(
    player_id: int,
    player_data: PlayerUpdate,
    db: Session = Depends(get_db)
):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    for field, value in player_data.dict(exclude_unset=True).items():
        setattr(player, field, value)
    
    db.commit()
    db.refresh(player)
    return player