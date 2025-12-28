from .auth_routes import router as auth_router
from .user_routes import router as user_router
from .item_routes import router as item_router
from .category_routes import router as category_router

__all__ = [
    "auth_router",
    "user_router",
    "item_router",
    "category_router"]