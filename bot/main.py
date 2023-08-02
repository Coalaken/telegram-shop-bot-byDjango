from aiogram import Bot, Dispatcher, executor

from misc.utils import STARTUP_MESSAGE


async def __on_startup() -> None:
    print(STARTUP_MESSAGE)


def start_bot():
    bot = Bot(token='6509866760:AAEJmL-XC-tetDGRfND1hUI5OmkIMLJFHao')
    dp = Dispatcher(bot)
    
    executor.start_polling(dp, skip_updates=True, on_startup=__on_startup)


