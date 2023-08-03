from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminAddItem(StatesGroup):
    name = State()
    img = State()
    description = State()
    price = State()
    

