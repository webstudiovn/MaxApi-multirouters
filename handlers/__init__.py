# app/handlers/__init__.py
__all__ = ("routers",)

from .commands import routers as commands_routers

# Объединяем все роутеры в один список
routers = [
    *commands_routers,
]