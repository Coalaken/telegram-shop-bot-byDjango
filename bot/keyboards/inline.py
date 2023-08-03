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