from fastapi import FastAPI
from app.api.endpoints import player

app = FastAPI(
    title="Survival Game API",
    description="API для игры на выживание",
    version="0.1.0"
)

app.include_router(
    player.router,
    prefix="/api/players",
    tags=["players"]
)