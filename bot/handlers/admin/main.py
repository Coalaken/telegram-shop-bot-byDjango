from decimal import Decimal

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from bot.states import AdminAddItem


def register_admin_handlers(dp: Dispatcher):
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
            print(message.photo[0].file_id)
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
            try:
                data['price'] = round(Decimal(message.text), 2)
            except Exception as e:
                await message.reply('invalid price! Try again!')
                await state.finish()                
        await state.finish()
        
    async def cancel(message: Message, state: FSMContext) -> None:
        current_state = state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Canceled')
        
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(add_item, commands=['add'], state=None)
    dp.register_message_handler(set_name, state=AdminAddItem.name)
    dp.register_message_handler(set_image, state=AdminAddItem.img, content_types=['photo'])
    dp.register_message_handler(set_description, state=AdminAddItem.description)
    dp.register_message_handler(set_price, state=AdminAddItem.price)