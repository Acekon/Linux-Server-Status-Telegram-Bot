import functools
import logging
import os

import aiogram


def auth_admin(func):
    @functools.wraps(func)
    async def wrapper(message=None, *args, **kwargs):
        admin_id = os.environ.get("admin")
        user_id = message.from_user.id
        user_first_name = message.from_user.first_name
        user_last_name = message.from_user.last_name
        if isinstance(message, aiogram.types.callback_query.CallbackQuery):
            user_command = message.data
        elif isinstance(message, aiogram.types.message.Message):
            if message.caption:
                user_command = f'img_upload_id:{message.caption}'
            else:
                user_command = message.text
        else:
            user_command = f'Not support message type logging: {type(message)}'
        logger.debug(f'user:{user_id};command:{user_command}')
        if str(user_id) != str(admin_id):
            logger.error(f'NOT PERMISSION: '
                         f'{user_id};{user_first_name};{user_last_name};{user_command}')
            return await message.answer(text=f'{user_first_name} you do not have permission')
        return await func(message, *args, **kwargs)

    return wrapper


def setup_logger():
    logger_ = logging.getLogger('bot_logger')

    if not logger_.handlers:
        logger_.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')

        access_log_handler = logging.FileHandler(filename='logs/bot.log', encoding='utf-8')
        access_log_handler.setLevel(logging.DEBUG)
        access_log_handler.setFormatter(formatter)
        logger_.addHandler(access_log_handler)

    return logger_


logger = setup_logger()
