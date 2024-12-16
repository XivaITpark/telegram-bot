from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ish Kerak'),KeyboardButton(text='SHerik Kerak')],[KeyboardButton(text='Hodim  Kerak')],[KeyboardButton(text='Ustoz Kerak')],[KeyboardButton(text='SHogrt  Kerak')],
    ],
    resize_keyboard=True
)