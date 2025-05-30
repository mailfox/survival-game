# /home/mailfox/survival-game/backend/main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Исправлено с fastapi.middleware
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