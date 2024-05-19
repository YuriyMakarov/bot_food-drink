from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    bd = ReplyKeyboardBuilder()
    for item in items:
        bd.add(KeyboardButton(text=item))
    return bd.as_markup(resize_keyboard=True)
