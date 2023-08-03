from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery

from bot.misc import GREETING, get_data_from_server
from bot.misc.utils import CATS_URL, ITEMS_URL, CATEGORY_MESSAGE
from bot.keyboards.inline import create_keyboard


def register_user_handlers(dp: Dispatcher, bot: Bot):
    
    @dp.message_handler(commands=['start', 'help'])
    async def first_commands(message: Message) -> None:
        await bot.send_message(message.from_user.id, GREETING)
    
    @dp.message_handler(commands=['categories'])
    async def show_categories(message: Message) -> None:
        data = await get_data_from_server(CATS_URL)
        cats = {int(cat.get('id')): cat.get('name') for cat in data}
        text = CATEGORY_MESSAGE
        await bot.send_message(message.from_user.id, text, reply_markup=create_keyboard(cats))
        
    @dp.callback_query_handler(Text(startswith='cat_', ignore_case=True))
    async def category_callback_handler(callback_query: CallbackQuery):
        cat_id = callback_query.data.split('_')[1]
        data = await get_data_from_server(ITEMS_URL, c_id=cat_id)
        await callback_query.answer(cache_time=1)
        for item in data:
            await callback_query.message.answer('Products by category:' + '\n'.join([item.get('name'), item.get('price')]))
    
    @dp.message_handler(commands=['products'])
    async def show_items(message: Message) -> None:
        data = await get_data_from_server(ITEMS_URL)
        for item in data:
            await bot.send_message(message.from_user.id, '\n'.join([item.get('name'), item.get('price')]))


