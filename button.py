from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


shop= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Porfimeriya',callback_data='porfimeriya'),InlineKeyboardButton(text='Koylaklar',callback_data='koylaklar')],
    ],
)

pardoz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Tush',callback_data='tush'),InlineKeyboardButton(text='Lak',callback_data='lak')],
         [InlineKeyboardButton(text='Pamada',callback_data='pamada'),InlineKeyboardButton(text='Qrem',callback_data='qrem')],
         [InlineKeyboardButton(text='Atr',callback_data='atr')]
    ]
)