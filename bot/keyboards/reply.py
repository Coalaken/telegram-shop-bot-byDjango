from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


buttons = [
    KeyboardButton(text='/help'),
    KeyboardButton(text='/categories'),
    KeyboardButton(text='/products'),
    
    # TO-DO make it only for admins
    KeyboardButton(text='/add')
]

menu_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(buttons[0]).row(buttons[1], buttons[2]).add(buttons[-1])