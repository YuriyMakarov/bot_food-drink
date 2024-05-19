from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Еда"),KeyboardButton(text="Напитки")]
    ],
    resize_keyboard=True,
    selective=True
)