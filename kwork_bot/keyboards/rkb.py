from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType
)

phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да✅"),
            KeyboardButton(text="Нет❎")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню⚙️")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)