from .player import router as player_router
from .items import router as items_router
from .inventory import router as inventory_router

__all__ = ["player_router", "items_router", "inventory_router"]
