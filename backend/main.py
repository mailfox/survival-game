from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routes import player, inventory, location

app = FastAPI()
init_db()  # Инициализация таблиц

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player.router)
app.include_router(inventory.router)
app.include_router(location.router)