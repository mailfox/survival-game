# /home/mailfox/survival-game/backend/models/player.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer
from database import Base

class PlayerDB(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    health = Column(Integer, default=100)
    hunger = Column(Integer, default=100)
    thirst = Column(Integer, default=100)
    radiation = Column(Integer, default=0)

class Player(BaseModel):
    health: int = 100
    hunger: int = 100
    thirst: int = 100
    radiation: int = 0

    class Config:
        from_attributes = True  # Добавлено