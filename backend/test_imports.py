# /home/mailfox/survival-game/backend/test_imports.py
import sys
import os

# Добавляем корень проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from models.item import ItemDB
    from models.player import PlayerDB
    print("Imports successful")
except ImportError as e:
    print(f"Import error: {e}")