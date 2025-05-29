from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from backend.core.database import get_db
from backend.core.models import Player

router = APIRouter()

def update_survival_stats(db: Session, player):
    now = datetime.utcnow()
    time_diff = now - player.last_update
    hours_passed = time_diff.total_seconds() / 3600
    
    player.hunger = max(0, player.hunger - int(5 * hours_passed))
    player.thirst = max(0, player.thirst - int(8 * hours_passed))
    
    if player.hunger == 0:
        player.health = max(0, player.health - int(2 * hours_passed))
    if player.thirst == 0:
        player.health = max(0, player.health - int(3 * hours_passed))
    
    player.last_update = now

@router.get("/player/{player_id}/status")
def get_player_status(player_id: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    update_survival_stats(db, player)
    db.commit()
    
    return {
        "health": player.health,
        "hunger": player.hunger,
        "thirst": player.thirst,
        "radiation": player.radiation,
        "status_effects": player.status_effects(),
        "is_alive": player.health > 0
    }