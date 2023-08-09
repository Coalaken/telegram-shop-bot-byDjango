from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def user_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        KeyboardButton(text='/help'),
        KeyboardButton(text='/categories'),
        KeyboardButton(text='/products'),
        KeyboardButton(text='/cart')
    ]
    return keyboard.add(buttons[0]).row(buttons[1], buttons[2]).add(buttons[3])
    
    
def admin_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        KeyboardButton(text='/edit'),
        KeyboardButton(text='/create_cat'),
        KeyboardButton(text='/add')
    ]
    return keyboard.add(buttons[0]).row(buttons[1], buttons[2])