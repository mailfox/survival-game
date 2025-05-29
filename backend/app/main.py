from fastapi import FastAPI
from backend.app.api.endpoints import player, survival
from backend.core.database import Base, engine

app = FastAPI()

app.include_router(player.router)
app.include_router(survival.router, prefix="/survival")

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)