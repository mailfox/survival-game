# /home/mailfox/survival-game/backend/models/item.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from typing import Optional

class ItemDB(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)  # weapon, food, medical
    weight = Column(Float)
    size_x = Column(Integer)
    size_y = Column(Integer)
    player_id = Column(Integer, ForeignKey("players.id"))
    icon_url = Column(String, nullable=True)

class Item(BaseModel):
    name: str
    type: str
    weight: float
    size: tuple[int, int]
    icon_url: Optional[str] = None

    class Config:
        from_attributes = True  # Изменено с orm_mode