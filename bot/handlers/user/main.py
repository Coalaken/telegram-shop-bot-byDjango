import json
from aiogram import Dispatcher, Bot
from aiogram.types import Message

from bot.misc import GREETING, get_data_from_server
from bot.misc.utils import CATS_URL, ITEMS_URL


def register_user_handlers(dp: Dispatcher, bot: Bot):
    
    @dp.message_handler(commands=['start', 'help'])
    async def first_commands(message: Message) -> None:
        await bot.send_message(message.from_user.id, GREETING)
    
    @dp.message_handler(commands=['categories'])
    async def show_categories(message: Message) -> None:
        data = await get_data_from_server(CATS_URL)
        cats = [cat.get('name') for cat in data]
        text = '\n'.join(cats)
        await bot.send_message(message.from_user.id, text)
        
    @dp.message_handler(commands=['products'])
    async def show_items(message: Message) -> None:
        data = await get_data_from_server(ITEMS_URL)
        for item in data:
            await bot.send_message(message.from_user.id, '\n'.join([item.get('name'), item.get('price')]))
            
    @dp.message_handler(commands=['by_category'])
    async def show_cat_items(message: Message) -> None:
        data = await get_data_from_server(ITEMS_URL, c_id=0)
        for item in data:
            await bot.send_message(message.from_user.id, 'Products by category:' + '\n'.join([item.get('name'), item.get('price')]))
            