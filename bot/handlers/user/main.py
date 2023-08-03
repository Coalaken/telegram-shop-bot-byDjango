from decimal import Decimal

from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from bot.misc import GREETING, get_data_from_server
from bot.misc.utils import CATS_URL, ITEMS_URL, CATEGORY_MESSAGE
from bot.keyboards.inline import create_keyboard
from bot.keyboards.reply import menu_keyboard
from bot.states import AdminAddItem


def register_user_handlers(dp: Dispatcher, bot: Bot):
    
    @dp.message_handler(commands=['start', 'help'])
    async def first_commands(message: Message) -> None:
        await bot.send_message(message.from_user.id, GREETING, reply_markup=menu_keyboard)
    
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
            await callback_query.message.answer('\n'.join([item.get('name'), item.get('price')]))
    
    @dp.message_handler(commands=['products'])
    async def show_items(message: Message) -> None:
        data = await get_data_from_server(ITEMS_URL)
        for item in data:
            await bot.send_message(message.from_user.id, '\n'.join([item.get('name'), item.get('price')]))
            
    @dp.message_handler(commands=['add'], state="*")
    async def add_item(message: Message) -> None:
        await AdminAddItem.name.set()
        await message.reply('Write the name!')            

    @dp.message_handler(state=AdminAddItem.name)
    async def set_name(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['name'] = message.text
        await AdminAddItem.next()
        await message.reply('Add an image')
        
    @dp.message_handler(state=AdminAddItem.img)
    async def set_image(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['img'] = message.photo[0].file_id
        await AdminAddItem.next()
        await message.reply('Add a description')

    @dp.message_handler(state=AdminAddItem.description)
    async def set_description(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['description'] = message.text
        await AdminAddItem.next()
        await message.reply('Set the price')
        
    @dp.message_handler(state=AdminAddItem.price)
    async def set_price(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['price'] = round(Decimal(message.text), 2)
        await state.finish()
        
    @dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
    async def cancel(message: Message, state: FSMContext) -> None:
        current_state = state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Canceled')