from fastapi import FastAPI
from game_core.api.routes import player_router, items_router, inventory_router

app = FastAPI()

app.include_router(player_router, prefix="/players", tags=["players"])
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(inventory_router)
