from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from handlers.control import auth_admin
from handlers.system import get_disk_space, get_ram_usage, get_cpu_usage

router = Router()


@router.message(Command(commands=['disk']))
@auth_admin
async def command_get_search(message: Message):
    disk_space = get_disk_space()
    await message.answer(f"{disk_space}")


@router.message(Command(commands=['ram']))
@auth_admin
async def command_get_search(message: Message):
    ram_usage = get_ram_usage()
    await message.answer(f"{ram_usage}")


@router.message(Command(commands=['cpu']))
@auth_admin
async def command_get_search(message: Message):
    cpu_usage = get_cpu_usage()
    await message.answer(f"{cpu_usage}")
