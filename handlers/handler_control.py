from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from handlers.control import auth_admin

router = Router()


@router.message(CommandStart())
@auth_admin
async def command_start_handler(message: Message) -> Message:
    return await message.answer(f"Hello, {hbold(message.from_user.full_name)}")
