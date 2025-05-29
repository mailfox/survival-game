from pydantic import BaseModel, Field

class PlayerBase(BaseModel):
    health: int = Field(100, ge=0, le=100)
    hunger: int = Field(100, ge=0, le=100)
    thirst: int = Field(100, ge=0, le=100)
    stamina: int = Field(100, ge=0, le=100)
    radiation: int = Field(0, ge=0, le=100)

class PlayerAction(BaseModel):
    player_id: int
    item_id: int