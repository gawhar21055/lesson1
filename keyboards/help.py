from aiogram.types import KeyboardButtonPollType
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_help_btns():
    btn1 = KeyboardButton(text="some text1")
    btn2 = KeyboardButton(text="some text2")
    btn3 = KeyboardButton(text="some text3")
    first_row = [btn1, btn2]
    second_row = [btn3]
    rows = [first_row, second_row]
    keyboard = ReplyKeyboardMarkup(
        keyboard=rows,
        resize_keyboard=True,
    )
    return keyboard


def get_help_keyboard():
    builder = ReplyKeyboardBuilder()
    for i in range(1, 11):  # 1-10
        # builder.button(text=f"some text {i}")
        builder.add(
            KeyboardButton(
                text=f"some text {i}",
            )
        )
    builder.adjust(2)
    return builder.as_markup()


def get_request_keyboard():
    builder = ReplyKeyboardBuilder()
    contact_btn = KeyboardButton(
        text="send my phone number",
        request_contact=True,
    )
    location_btn = KeyboardButton(
        text="send my location",
        request_location=True,
    )
    poll_btn = KeyboardButton(
        text="send my poll",
        request_poll=KeyboardButtonPollType(
            type="quiz",
        ),
    )
    builder.row(contact_btn, location_btn, poll_btn)
    # builder.adjust(2)
    return builder.as_markup(
        resize_keyboard=True,
    )
