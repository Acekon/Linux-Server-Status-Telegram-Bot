import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv

from handlers import handler_sys_info, handler_control

dp = Dispatcher()
load_dotenv()
bot_token = f'{os.environ.get("bot_token")}'
if os.environ.get("proxy"):
    session = AiohttpSession(proxy=os.environ.get("proxy"))
else:
    session = None


async def main() -> None:
    dp.include_router(handler_sys_info.router)
    dp.include_router(handler_control.router)
    bot = Bot(token=bot_token, session=session, parse_mode='HTML')
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        SystemExit('Stopped')
