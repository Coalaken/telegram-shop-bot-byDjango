import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from bot.misc import print_success_message
from bot.handlers.user import register_user_handlers
from bot.handlers.admin import register_admin_handlers 
from bot.misc.env import TgKeys   

    
async def __on_startup(_) -> None:
    await print_success_message()
    
    
def start_bot(): 
    bot = Bot(token=TgKeys.TOKEN, parse_mode='html')
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_user_handlers(dp, bot)    
    register_admin_handlers(dp, bot)

    executor.start_polling(dp, skip_updates=True, on_startup=__on_startup)


