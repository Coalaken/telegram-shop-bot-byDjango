from decimal import Decimal

from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from bot.states import AdminAddItem, AdminAddCat, AdminUpdateItem
from bot.misc.fetch_data import create_category, create_item, get_data_from_server
from bot.misc.utils import (
    CATS_URL,
    ADMIN_ID,
    ITEMS_URL,
    ITEM_UPDATE_URL,
    ITEM_DELETE_URL
)
from bot.keyboards.inline import delete_update_item_keyboard, update_keyboard
from bot.misc import delete_item, update_item


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
        
    """
    Edit items
    """
    @auth
    async def edit_items(message: Message) -> None:
        data = await get_data_from_server(ITEMS_URL)
        for item in data:
            try:
                await bot.send_photo(message.from_user.id, item['img'], f"{item['name']}\n ${item['price']}",
                                     reply_markup=delete_update_item_keyboard(item.get('id')))
            except Exception as e:
                await bot.send_message(message.from_user.id, f"{item['name']}\n ${item['price']}",
                                       reply_markup=delete_update_item_keyboard(item.get('id')))
                
    """
    Delete item
    """
    async def delete_callback(callback_query: CallbackQuery) -> None:
        item_id = int(callback_query.data.split('_')[1])
        await delete_item(ITEM_DELETE_URL, item_id)
        await callback_query.message.answer('Deleted')
        
    """
    Update item
    """
    async def update_callback(callback_query: CallbackQuery, state: FSMContext) -> None:
        item_id = callback_query.data.split('_')[1]
        await AdminUpdateItem.start.set()
        async with state.proxy() as data:
            data['id'] = item_id
        await callback_query.answer()
        await callback_query.message.answer('Зick something >>>', reply_markup=update_keyboard())
        
    """
    Update name
    """
    async def set_name_state(callback_query: CallbackQuery) -> None:
        await callback_query.message.answer('Name:')
        await AdminUpdateItem.name.set()
        await callback_query.answer()
        
    async def set_item_name(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data: 
            data['name'] = message.text.lower()    
        await AdminUpdateItem.price.set()
    
    """
    Update price
    """        
    async def set_price_state(callback_query: CallbackQuery) -> None:
        await callback_query.message.answer('Price:')
        await AdminUpdateItem.price.set()
        await callback_query.answer()
        
    async def set_item_price(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['price'] = float(round(Decimal(message.text.strip()), 2))
        await AdminUpdateItem.start.set()
    
    """
    Update description
    """
    async def set_desc_sate(callback_query: CallbackQuery) -> None:
        await callback_query.message.answer('Description:')        
        await AdminUpdateItem.description.set()
        await callback_query.answer()
        
    async def set_item_description(message: Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['description'] = message.text
    
    """
    Update image
    """         
    async def set_img_state(callback_query: CallbackQuery) -> None:
        await callback_query.message.answer('IMG:')
        await AdminUpdateItem.img.set()
        await callback_query.answer()
         
    async def set_item_img(message: Message, state: FSMContext):
        async with state.proxy() as data:
            data['img'] = message.photo[0].file_id
            
    """
    Save
    """
    async def save_(callback_query: CallbackQuery) -> None:
        await AdminUpdateItem.save.set()
        await callback_query.answer('[y/N]', show_alert=True)
        
    async def save_updates(message: Message, state: FSMContext):
        if message.text.lower() == 'y':
            async with state.proxy() as data: 
                expected = ['name', 'price', 'descriproin', 'img']
                item_data = {}
                for el in expected:
                    if el in data.keys():
                        item_data[el] = data.get(el)
            await update_item(ITEM_UPDATE_URL, data['id'], item_data)
            await state.finish()
        else:
            await AdminUpdateItem.start.set()
            
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(add_item, commands=['add'], state=None)
    dp.register_message_handler(set_name, state=AdminAddItem.name)
    dp.register_message_handler(set_image, state=AdminAddItem.img, content_types=['photo'])
    dp.register_message_handler(set_description, state=AdminAddItem.description)
    dp.register_message_handler(set_price, state=AdminAddItem.price)
    dp.register_message_handler(add_category, commands=['create_cat'], state=None)
    dp.register_message_handler(set_category_name, state=AdminAddCat.name, content_types=['text'])
    dp.register_message_handler(edit_items, commands=['edit'])
    dp.register_callback_query_handler(delete_callback, Text(startswith='delete_', ignore_case=True))
    dp.register_callback_query_handler(update_callback, Text(startswith='update_', ignore_case=True))
    
    dp.register_callback_query_handler(set_name_state, Text(equals='state_name'), state="*")
    dp.register_message_handler(set_item_name, state=AdminUpdateItem.name)
    
    dp.register_callback_query_handler(set_price_state, Text(equals='state_price', ignore_case=True), state="*")
    dp.register_message_handler(set_item_price, state=AdminUpdateItem.price)
    
    dp.register_callback_query_handler(set_desc_sate, Text(equals='state_desc', ignore_case=True), state="*")
    dp.register_message_handler(set_item_description, state=AdminUpdateItem.description)
    
    dp.register_callback_query_handler(set_img_state, Text(equals='state_img', ignore_case=True), state="*")
    dp.register_message_handler(set_item_img, state=AdminUpdateItem.img, content_types=['photo'])
    
    dp.register_callback_query_handler(save_, Text(equals='state_save', ignore_case=True), state="*")
    dp.register_message_handler(save_updates, state=AdminUpdateItem.save)
    
    # TO-DO 
    # - price validator
    # - other validators 
    # - docker+
    # - redis Memory