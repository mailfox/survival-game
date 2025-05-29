from backend.core.database import Base, engine, SessionLocal
from backend.core.models import Player
from datetime import datetime

def init_db():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        if db.query(Player).count() == 0:
            test_player = Player(
                id=1,
                health=100,
                hunger=100,
                thirst=100,
                stamina=100,
                radiation=0,
                last_update=datetime.utcnow()
            )
            db.add(test_player)
            db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()