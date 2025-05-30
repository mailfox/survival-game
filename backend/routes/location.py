# /home/mailfox/survival-game/backend/routes/location.py
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db  # Абсолютный импорт
from models.item import ItemDB  # Абсолютный импорт
from models.player import PlayerDB  # Абсолютный импорт
import random

router = APIRouter(prefix="/location", tags=["location"])

@router.post("/explore")
async def explore(data: dict = Body(...), db: Session = Depends(get_db)):
    location_name = data.get("location_name")
    player_id = data.get("player_id", 1)
    if not location_name:
        raise HTTPException(status_code=422, detail="location_name is required")
    
    locations = {
        "Bunker": ["Medkit", "Ration", None],
        "Forest": ["Berry", "Water", None],
        "Factory": ["Bandage", None]
    }
    
    if location_name not in locations:
        raise HTTPException(status_code=404, detail="Location not found")
    
    found = random.choice(locations[location_name])
    danger = random.choice([None, "Radiation", "Mutant"]) if found else None
    
    if found:
        item = ItemDB(
            name=found,
            type="resource",
            weight=1.0,
            size_x=1,
            size_y=1,
            player_id=player_id,
            icon_url=f"/images/{found.lower()}.png"  # Автоматический icon_url
        )
        db.add(item)
    
    if danger == "Radiation":
        player = db.query(PlayerDB).filter(PlayerDB.id == player_id).first()
        if player:
            player.radiation = min(player.radiation + 10, 100)
            if player.radiation > 50:
                player.health = max(0, player.health - 5)
            if player.health == 0:
                raise HTTPException(status_code=400, detail="Player died from radiation")
    
    db.commit()
    
    return {
        "success": found is not None,
        "found": found,
        "danger": danger
    }