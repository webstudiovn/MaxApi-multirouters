from maxapi import Router
from maxapi.types import BotStarted, Command, MessageCreated

router = Router()

@router.bot_started()
async def bot_started(event: BotStarted):
    await event.bot.send_message(
        chat_id=event.chat_id,
        text=(f"Добро пожаловать в чат-бот для знакомств.\n"
              f"Отправьте /start, чтобы начать поиск подходящей анкеты")
    )

@router.message_created(Command("start"))
async def start_search(event: MessageCreated):
    await event.message.answer("Поиск...")
