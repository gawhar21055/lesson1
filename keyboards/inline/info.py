from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_info_keyboard():
    # btn1 = InlineKeyboardButton(
    #     text="info",
    #     url="https://t.me/paul",
    # )
    # first_row = [btn1]
    # rows = [first_row]
    # markup = InlineKeyboardMarkup(inline_keyboard=rows)
    # return markup
    builder = InlineKeyboardBuilder()
    for index in range(1, 11):
        builder.button(
            text=f"info {index}",
            callback_data=str(index),
        )
    builder.adjust(2)
    return builder.as_markup()
