import asyncio
import subprocess
from aiogram import Bot, Dispatcher, executor

from bot.misc import print_success_message

    
    
async def __on_startup(_) -> None:
    await print_success_message()


def start_bot():
    bot = Bot(token='6509866760:AAEJmL-XC-tetDGRfND1hUI5OmkIMLJFHao')
    dp = Dispatcher(bot)
    
    executor.start_polling(dp, skip_updates=True, on_startup=__on_startup)


