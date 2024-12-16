import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, callback_query
from canfig import BOT_TOKEN as token
from button import *

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer_photo(
        photo='https://kosmetista.ru/uploads/images/06/29/96/2024/08/24/c31a1f_lbox.jpg',caption='Ayyollar uchun', reply_markup=shop)


@dp.callback_query(F.data == 'porfimeriya')
async def maxs(call: CallbackQuery):
    await call.message.answer_photo(
        photo='https://podrobno.uz/upload/iblock/a32/kosmetika.jpg',caption='ayollar maxsulotlari',reply_markup=pardoz)

@dp.callback_query(F.data == 'tush')
async def maxs(call: CallbackQuery):
    await call.message.answer_photo(
        photo='https://daryo.uz/cache/2022/04/photo_2022-04-10_00-39-01-640x640.jpg',caption='tush',reply_markup=pardoz)

@dp.callback_query(F.data == 'lak')
async def maxs(call: CallbackQuery):
    await call.message.answer_photo(
        photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8BnUcrOVcFDJ55cfZfZ9v_cHBCX9L4FZXbg&s',caption='lak',reply_markup=pardoz)

@dp.callback_query(F.data == 'pamada')
async def maxs(call: CallbackQuery):
    await call.message.answer_photo(
        photo='https://images.faberlic.com/images/fl/TflGoods/md/1001041177038_17065345993.jpg',caption='pamada',reply_markup=pardoz)


@dp.callback_query(F.data == 'qrem')
async def maxs(call: CallbackQuery):
    await call.message.answer_photo(
        photo='https://mineralsplanet.ru/7114-thickbox_default/mineralnaya-pudra-spf15-30-belosnezhnaya.jpg',caption='qrem',reply_markup=pardoz)


@dp.callback_query(F.data == 'atr')
async def maxs(call: CallbackQuery):
    await call.message.answer_photo(
        photo='https://st4.depositphotos.com/14378538/19764/i/450/depositphotos_197641066-stock-photo-rose-flower-essential-oil-spa.jpg',caption='atr',reply_markup=pardoz)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
