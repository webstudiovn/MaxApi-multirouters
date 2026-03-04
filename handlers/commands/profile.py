from maxapi import Router
from maxapi.types import Command, MessageCreated

router = Router()
@router.message_created(Command("profile"))
async def update_profile(event: MessageCreated):
    await event.message.answer("Update profile")
