from sqlalchemy import Column, Integer, DateTime
from .database import Base
from datetime import datetime

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    health = Column(Integer, default=100)
    hunger = Column(Integer, default=100)
    thirst = Column(Integer, default=100)
    stamina = Column(Integer, default=100)
    radiation = Column(Integer, default=0)
    last_update = Column(DateTime, default=datetime.utcnow)

    def status_effects(self):
        effects = []
        if self.hunger < 20:
            effects.append("starving")
        if self.thirst < 20:
            effects.append("dehydrated")
        if self.radiation > 50:
            effects.append("irradiated")
        return effects