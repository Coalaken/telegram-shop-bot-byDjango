from typing import Dict

from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery, InputMedia

from bot.misc import (
    get_data_from_server,
    get_user_cart,
    qadd_to_cart,
    qdelete_from_cart,
)
from bot.misc.utils import (
    CART_URL,
    CATS_URL,
    ITEMS_URL,
    CATEGORY_MESSAGE, 
    GREETING,
    CART_ADD_URL,
    CART_DEL_URL,
)
from bot.keyboards.inline import (
    buy_delete_cart,
    create_keyboard,
    buy_add_cart,
    produts_navigation,
)
from bot.keyboards.reply import user_keyboard, admin_keyboard


def register_user_handlers(dp: Dispatcher, bot: Bot):
    
    async def admin(message: Message) -> None:
        await message.answer('OK!', reply_markup=admin_keyboard())
        await message.delete()

    async def first_commands(message: Message) -> None:
        await bot.send_message(message.from_user.id, GREETING, reply_markup=user_keyboard())
        await message.delete()

    async def show_categories(message: Message) -> None:
        data = await get_data_from_server(CATS_URL)
        cats = {int(cat.get('id')): cat.get('name') for cat in data}
        text = CATEGORY_MESSAGE
        await bot.send_message(message.from_user.id, text, reply_markup=create_keyboard(cats))
        await message.delete()

    async def category_callback_handler(callback_query: CallbackQuery):
        cat_id = callback_query.data.split('_')[1]
        data = await get_data_from_server(ITEMS_URL, c_id=cat_id)
        await callback_query.answer(cache_time=1)
        for item in data:
            try:
                await bot.send_photo(callback_query.from_user.id,
                                    item['img'],
                                    f"{item['name']}\n ${item['price']}",
                                    reply_markup=buy_add_cart(item['id'],
                                                              callback_query.from_user.id))
            except Exception as e:
                await bot.send_message(callback_query.from_user.id,
                                       f"{item['name']}\n ${item['price']}",
                                       reply_markup=buy_add_cart(item['id'],
                                                                 callback_query.from_user.id))

    async def show_items(message: Message) -> None:
        data = await get_data_from_server(ITEMS_URL)
        for item in data:
            try:
                await bot.send_photo(message.from_user.id,
                                    item['img'],
                                    f"{item['name']}\n ${item['price']}",
                                    reply_markup=buy_add_cart(item['id'],
                                                              message.from_user.id))
            except Exception as e:
                await bot.send_message(message.from_user.id,
                                       f"{item['name']}\n ${item['price']}",
                                       reply_markup=buy_add_cart(item['id'],
                                                                 message.from_user.id))

    async def get_cart(message: Message) -> None:
        await message.answer('Your cart:')
        resp = await get_user_cart(CART_URL, message.from_user.id)
        total_price = 0
        for item in resp['products']:
            total_price += float(item['price'])
            try:
                await bot.send_photo(message.from_user.id,
                                     item['img'],
                                     f"{item['name']}\n${item['price']}",
                                     reply_markup=buy_delete_cart(item['id'],
                                                                  message.from_user.id))
            
            except Exception:
                await message.answer(f"{item['name']}\n${item['price']}",
                                     reply_markup=buy_delete_cart(item['id'],
                                                                  message.from_user.id))
        await message.answer(f'Total price:\n{total_price}')
 
    async def add_to_cart(callback_query: CallbackQuery) -> None:
        await callback_query.answer()
        data = callback_query.data.split('_') 
        await qadd_to_cart(CART_ADD_URL,
                           data[-2],
                           data[-1])
        
    async def buy(callback_query: CallbackQuery) -> None:
        pass
    
    async def delete_from_cart(callback_query: CallbackQuery) -> None:
        data = callback_query.data.split('_')
        await callback_query.answer()
        await qdelete_from_cart(CART_DEL_URL,
                                data[-2],
                                data[-1],
                                )
    
    
    async def products2(message: Message) -> None:
        products = await get_data_from_server(ITEMS_URL)
        last = len(products) - 1
        try: 
            await bot.send_photo(message.from_user.id,
                                 products[0]['img'],
                                 f"<b>{products[0]['name']}</b>" +
                                 f"\n${products[0]['price']}" +
                                 f'<i>\n{1} of {last + 1}</i>',
                                 reply_markup=produts_navigation(0, last=last))
        except Exception:
            await bot.send_message(message.from_user.id,
                                 f"<b>{products[0]['name']}</b>" +
                                 f"\n${products[0]['price']}" +
                                 f'<i>\n{1} of {last + 1}</i>',
                                 reply_markup=produts_navigation(0, last=last))
            
    async def button(callback_query: CallbackQuery) -> None:
        current_index = int(callback_query.data.split('_')[1])
        products = await get_data_from_server(ITEMS_URL)
        last = len(products) - 1 
        
        if not products[current_index]['img']:
            await callback_query.message.edit_reply_markup(produts_navigation(current_index, last=last))
        
        await callback_query.answer()
        try:
            await callback_query.message.edit_media(InputMedia(media=products[current_index]['img'],
                                                           caption=f"<b>{products[current_index]['name']}</b>" +
                                                           f"\n${products[current_index]['price']}" +
                                                           f'<i>\n{current_index + 1} of {last + 1}</i>'),
                                                reply_markup=produts_navigation(current_index, last=last),)
        except:
            return
            
                
    dp.register_message_handler(products2, commands=['products'])
    dp.register_callback_query_handler(button, Text(startswith='index_'))
    
    dp.register_message_handler(admin, commands=['admin'])

    dp.register_message_handler(first_commands, commands=['start', 'help'])
    dp.register_message_handler(show_categories, commands=['categories'])
    dp.register_callback_query_handler(category_callback_handler, Text(startswith='cat_', ignore_case=True))
    # dp.register_message_handler(show_items, commands=['products'])

    dp.register_message_handler(get_cart, commands=['cart'])
    dp.register_callback_query_handler(add_to_cart, Text(startswith='atc_', ignore_case=True))
    dp.register_callback_query_handler(delete_from_cart, Text(startswith='cd_', ignore_case=True))
    dp.register_callback_query_handler(buy, Text(startswith='buy_', ignore_case=True))
    

    
    