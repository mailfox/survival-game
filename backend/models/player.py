from sqlalchemy import Column, Integer
from db.base_class import Base

class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    health = Column(Integer, default=100)
    hunger = Column(Integer, default=100)
    thirst = Column(Integer, default=100)
    stamina = Column(Integer, default=100) 
    radiation = Column(Integer, default=0) 