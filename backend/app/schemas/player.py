from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PlayerBase(BaseModel):
    id: int
    health: int = 100
    hunger: int = 100
    thirst: int = 100
    stamina: int = 100
    radiation: int = 0
    last_update: datetime

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(BaseModel):
    health: Optional[int] = None
    hunger: Optional[int] = None
    thirst: Optional[int] = None
    stamina: Optional[int] = None
    radiation: Optional[int] = None