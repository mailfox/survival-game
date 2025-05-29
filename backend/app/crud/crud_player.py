from sqlalchemy.orm import Session
from app.db.models import Player

def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.id == player_id).first()

def create_player(db: Session):
    db_player = Player()
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player