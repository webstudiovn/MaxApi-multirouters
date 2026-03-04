import asyncio
import logging
from maxapi import Bot, Dispatcher
from app.config.settings import settings
from app.handlers import routers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.token.max_api)
dp = Dispatcher()

async def main() -> None:
    # Правильный способ подключения роутера к диспетчеру
    dp.include_routers(*routers)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")