from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


buttons = [
    KeyboardButton(text='/help'),
    KeyboardButton(text='/categories'),
    KeyboardButton(text='/products')
]

menu_keyboard = ReplyKeyboardMarkup().add(*buttons)