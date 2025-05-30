# /home/mailfox/survival-game/backend/routes/inventory.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.item import Item, ItemDB  # Абсолютный импорт
from database import get_db  # Абсолютный импорт

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/{player_id}")
async def get_inventory(player_id: int, db: Session = Depends(get_db)):
    items = db.query(ItemDB).filter(ItemDB.player_id == player_id).all()
    if not items:
        return {"items": []}
    return {
        "items": [
            {
                "id": item.id,
                "name": item.name,
                "type": item.type,
                "weight": item.weight,
                "size": [item.size_x, item.size_y],
                "icon_url": item.icon_url
            } for item in items
        ]
    }

@router.post("/add")
async def add_item(item: Item, player_id: int, db: Session = Depends(get_db)):
    db_item = ItemDB(**item.dict(), player_id=player_id)
    db.add(db_item)
    db.commit()
    return {"message": "Item added"}

@router.delete("/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}