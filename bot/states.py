from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminAddItem(StatesGroup):
    name = State()
    img = State()
    description = State()
    price = State()
    

class AdminAddCat(StatesGroup):
    name = State()

class AdminUpdateItem(StatesGroup):
    start = State()
    name = State()
    img = State()
    description = State()
    price = State()
    save = State()