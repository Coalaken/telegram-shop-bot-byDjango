from typing import Dict, List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_buttons(buttons_name: Dict[int, str]) -> List[InlineKeyboardButton]:
    buttons = list()
    for cat_id, name in buttons_name.items():
        button = InlineKeyboardButton(text=name.lower(),
                                      callback_data=f'cat_{cat_id}')
        buttons.append(button)
    return buttons


def create_keyboard(buttons_name: Dict[int, str]) -> InlineKeyboardMarkup:
    buttons = create_buttons(buttons_name)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

def delete_update_item_keyboard(item_id: int) -> InlineKeyboardMarkup:
    delete = InlineKeyboardButton(text='Delete', callback_data=f'delete_{item_id}')
    update = InlineKeyboardButton(text='Update', callback_data=f'update_{item_id}')
    
    keyboard = InlineKeyboardMarkup().add(delete, update)
    return keyboard


def buy_add_cart(item_id: int, user_id):
    add = InlineKeyboardButton(text='+', callback_data=f'atc_{user_id}_{item_id}')
    buy = InlineKeyboardButton(text='buy', callback_data=f'buy_{item_id}')

    keyboard = InlineKeyboardMarkup(row_width=1).row(add, buy)
    return keyboard


def buy_delete_cart(item_id: int, user_id):
    buy = InlineKeyboardButton(text='buy', callback_data=f'buy_{item_id}')
    delete = InlineKeyboardButton(text='delete', callback_data=f'cd_{user_id}_{item_id}')

    return InlineKeyboardMarkup().row(buy, delete)
