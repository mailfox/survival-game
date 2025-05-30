from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class ItemDB(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)  # weapon, food, medical
    weight = Column(Float)
    size_x = Column(Integer)
    size_y = Column(Integer)
    player_id = Column(Integer, ForeignKey("players.id"))  # Связь с игроком

class Item(BaseModel):
    name: str
    type: str
    weight: float
    size: tuple[int, int]