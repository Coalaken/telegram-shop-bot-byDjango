from decimal import Decimal

from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from bot.states import AdminAddItem, AdminAddCat
# from bot.database.methods.create import create_product
from bot.misc.fetch_data import create_category, create_item
from bot.misc.utils import CATS_URL, ADMIN_ID, ITEMS_URL


def auth(func):
    async def wrapper(message: Message, state: FSMContext=None):
        if message.from_user.id != ADMIN_ID:
            await message.answer('Permission denied...')
            return 
        return await func(message)
    return wrapper


def register_admin_handlers(dp: Dispatcher, bot: Bot):
    
    """
    Product creation process
    """
    @auth
    async def add_item(message: Message) -> None:
        await AdminAddItem.name.set()
        await message.reply('Write the name!')            

    async def set_name(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['name'] = message.text
        await AdminAddItem.next()
        await message.reply('Add an image')
        
    async def set_image(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            # print(message.photo[0].file_id)
            data['img'] = message.photo[0].file_id
        await AdminAddItem.next()
        await message.reply('Add a description')    
        
    async def set_description(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['description'] = message.text
        await AdminAddItem.next()
        await message.reply('Set the price')
        
    async def set_price(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            # try:
            data['price'] = float(round(Decimal(message.text.strip()), 2))
            await create_item(ITEMS_URL, data)
            await message.reply('Created!')
            # except Exception as e:
            #     print(e)
            #     await message.reply('invalid price! Try again!')
            #     await state.finish()               

        await state.finish()
        
    """
    Category creation process
    """
    @auth
    async def add_category(message: Message) -> None:
        await AdminAddCat.name.set()
        await message.answer('Set the name')
        
    async def set_category_name(message: Message, state: FSMContext) -> None:
        await create_category(CATS_URL, message.text)
        await state.finish()
    
    """
    Function that stops any process
    """
    async def cancel(message: Message, state: FSMContext) -> None:
        current_state = state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply(f'Canceled by user_id {message.from_user.id}')
        
        
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(add_item, commands=['add'], state=None)
    dp.register_message_handler(set_name, state=AdminAddItem.name)
    dp.register_message_handler(set_image, state=AdminAddItem.img, content_types=['photo'])
    dp.register_message_handler(set_description, state=AdminAddItem.description)
    dp.register_message_handler(set_price, state=AdminAddItem.price)
    dp.register_message_handler(add_category, commands=['create_cat'], state=None)
    dp.register_message_handler(set_category_name, state=AdminAddCat.name, content_types=['text'])
