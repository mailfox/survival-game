# /home/mailfox/survival-game/backend/routes/player.py
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from models.player import Player, PlayerDB  # Абсолютный импорт
from database import get_db  # Абсолютный импорт

router = APIRouter(prefix="/player", tags=["player"])

@router.get("/{id}", response_model=Player)
async def get_player(id: int, db: Session = Depends(get_db)):
    player = db.query(PlayerDB).filter(PlayerDB.id == id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.post("/eat")
async def eat(data: dict = Body(...), db: Session = Depends(get_db)):
    player_id = data.get("player_id")
    amount = data.get("amount")
    if player_id is None or amount is None:
        raise HTTPException(status_code=422, detail="player_id and amount are required")
    player = db.query(PlayerDB).filter(PlayerDB.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    player.hunger = min(player.hunger + amount, 100)
    db.commit()
    return {"hunger": player.hunger}

@router.post("/drink")
async def drink(data: dict = Body(...), db: Session = Depends(get_db)):
    player_id = data.get("player_id")
    amount = data.get("amount")
    if player_id is None or amount is None:
        raise HTTPException(status_code=422, detail="player_id and amount are required")
    player = db.query(PlayerDB).filter(PlayerDB.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    player.thirst = min(player.thirst + amount, 100)
    db.commit()
    return {"thirst": player.thirst}

@router.post("/{player_id}/radiate")
async def radiate_player(player_id: int, data: dict = Body(...), db: Session = Depends(get_db)):
    amount = data.get("amount", 10)
    player = db.query(PlayerDB).filter(PlayerDB.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    player.radiation = min(player.radiation + amount, 100)
    if player.radiation > 50:
        player.health = max(0, player.health - 5)
    if player.health == 0:
        raise HTTPException(status_code=400, detail="Player died from radiation")
    
    db.commit()
    db.refresh(player)
    return player