from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.item import ItemDB
import random

router = APIRouter()

@router.post("/location/explore")
async def explore(data: dict = Body(...), db: Session = Depends(get_db)):
    location_name = data.get("location_name")
    player_id = data.get("player_id", 1)  # По умолчанию игрок с id=1
    if not location_name:
        raise HTTPException(status_code=422, detail="location_name is required")
    
    # Пример логики исследования локации
    locations = {
        "Bunker": ["Medkit", "Ration", None],
        "Forest": ["Wood", "Berry", None],
        "Factory": ["Scrap", "Tool", None]
    }
    
    if location_name not in locations:
        raise HTTPException(status_code=404, detail="Location not found")
    
    found = random.choice(locations[location_name])
    danger = random.choice([None, "Radiation", "Mutant"]) if found else None
    
    if found:
        # Добавление предмета в инвентарь
        item = ItemDB(
            name=found,
            type="resource",
            weight=1.0,
            size_x=1,
            size_y=1,
            player_id=player_id
        )
        db.add(item)
        db.commit()
    
    return {
        "success": found is not None,
        "found": found,
        "danger": danger
    }