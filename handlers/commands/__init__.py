__all__ = ("routers",)

from .base_commands import router as base_commands_router
from .profile import router as profile_router
# Собираем все роутеры команд в список
routers = [
    base_commands_router,
    profile_router
]