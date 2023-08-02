from aiogram import Bot, Dispatcher, executor

from bot.misc import print_success_message
from bot.handlers.user import register_user_handlers
    
    
async def __on_startup(_) -> None:
    await print_success_message()



# bot = Bot(token='6509866760:AAEJmL-XC-tetDGRfND1hUI5OmkIMLJFHao')
# dp = Dispatcher(bot)
    
    
def start_bot(): 
    bot = Bot(token='6509866760:AAEJmL-XC-tetDGRfND1hUI5OmkIMLJFHao')
    dp = Dispatcher(bot)   
    
    register_user_handlers(dp, bot)
    
    executor.start_polling(dp, skip_updates=True, on_startup=__on_startup)


