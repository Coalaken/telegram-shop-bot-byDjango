from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_buttons(buttons_name: List[str]) -> List[InlineKeyboardButton]:
    buttons = list()
    for name in buttons_name:
        button = InlineKeyboardButton(text=name.lower(),
                                      callback_data=f'btn_{name.lower()}')
        buttons.append(button)
    return buttons


def create_keyboard(buttons_name: List[str]) -> InlineKeyboardMarkup:
    buttons = create_buttons(buttons_name)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard