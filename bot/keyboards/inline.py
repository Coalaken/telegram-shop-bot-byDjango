from typing import Dict, List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


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


def update_keyboard():
    keyboard = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton(text='name', callback_data='state_name'),
        InlineKeyboardButton(text='img', callback_data='state_img'),
        InlineKeyboardButton(text='description', callback_data='state_desc'),
        InlineKeyboardButton(text='price', callback_data='state_price'),
        InlineKeyboardButton(text='save', callback_data='state_save')
    ]
    return keyboard.row(buttons[0], buttons[1]).row(buttons[2], buttons[3]).add(buttons[-1])


# product_index_cb = CallbackData('get_all_products', 'index')


def produts_navigation(current_index: int, last: int):
    # of = InlineKeyboardButton(text=f"{current_index + 1} of {last + 1}"),
    left = InlineKeyboardButton(text='Previous', callback_data=f"index_{current_index - 1 if current_index - 1 > -1 else 0}")
    right = InlineKeyboardButton(text='Next', callback_data=f'index_{current_index + 1 if current_index + 1 <= last else last}')
    ikb = InlineKeyboardMarkup(row_width=1).row(left, right)
    return ikb