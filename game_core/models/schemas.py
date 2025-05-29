from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str
    health: int = 100
    level: int = 1

class ItemCreate(BaseModel):
    name: str
    type: str
    value: int

class InventoryItem(BaseModel):
    id: int
    name: str
    type: str
    quantity: int = 1
