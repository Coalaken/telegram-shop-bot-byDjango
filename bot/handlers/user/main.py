from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery

from bot.misc import GREETING, get_data_from_server, delete_item
from bot.misc.utils import CATS_URL, ITEMS_URL, CATEGORY_MESSAGE, ITEM_DELETE_URL
from bot.keyboards.inline import create_keyboard, delete_update_item_keyboard
from bot.keyboards.reply import menu_keyboard


def register_user_handlers(dp: Dispatcher, bot: Bot):

    async def first_commands(message: Message) -> None:
        await bot.send_message(message.from_user.id, GREETING, reply_markup=menu_keyboard)

    async def show_categories(message: Message) -> None:
        data = await get_data_from_server(CATS_URL)
        cats = {int(cat.get('id')): cat.get('name') for cat in data}
        text = CATEGORY_MESSAGE
        await bot.send_message(message.from_user.id, text, reply_markup=create_keyboard(cats))

    async def category_callback_handler(callback_query: CallbackQuery):
        cat_id = callback_query.data.split('_')[1]
        data = await get_data_from_server(ITEMS_URL, c_id=cat_id)
        await callback_query.answer(cache_time=1)
        for item in data:
            await callback_query.message.answer('\n'.join([item.get('name'), item.get('price')]))

    async def show_items(message: Message) -> None:
        data = await get_data_from_server(ITEMS_URL)
        for item in data:
            try:
                await bot.send_photo(message.from_user.id,
                                    item['img'],
                                    f"{item['name']}\n ${item['price']}")
            except Exception as e:
                await bot.send_message(message.from_user.id, f"{item['name']}\n ${item['price']}")

    # TO-DO: Write edit admin function
    async def edit_items(message: Message) -> None:
        data = await get_data_from_server(ITEMS_URL)
        for item in data:
            try:
                await bot.send_photo(message.from_user.id, item['img'], f"{item['name']}\n ${item['price']}",
                                     reply_markup=delete_update_item_keyboard(item.get('id')))
            except Exception as e:
                await bot.send_message(message.from_user.id, f"{item['name']}\n ${item['price']}",
                                       reply_markup=delete_update_item_keyboard(item.get('id')))

    async def delete_callback(callback_query: CallbackQuery) -> None:
        item_id = callback_query.data.split('_')[1]
        await delete_item(ITEM_DELETE_URL, item_id)
        await callback_query.message.answer('Deleted')

    async def update_callback(callback_query: CallbackQuery) -> None:
        item_id = callback_query.data.split('_')[1]
        # TO-DO: function that upd item
        pass

    dp.register_message_handler(first_commands, commands=['start', 'help'])
    dp.register_message_handler(show_categories, commands=['categories'])
    dp.register_callback_query_handler(category_callback_handler, Text(startswith='cat_', ignore_case=True))
    dp.register_message_handler(show_items, commands=['products'])

    dp.register_message_handler(edit_items, commands=['edit'])
    dp.register_callback_query_handler(delete_callback, Text(startswith='delete_', ignore_case=True))



    
    