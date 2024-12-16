import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from confing import BOT_TOKEN
from aiogram.fsm.context import FSMContext
from state import *
from button import *

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def CommandStart(message: Message):
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menu)


@dp.message(F.text == 'Ish Kerak')
async def start_ism(message: Message, state: FSMContext):
    await state.set_state(US.ism_k)
    await message.answer(text='Ismni Kiriting')


@dp.message(US.ism_k)
async def get_ism(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await message.answer(text='Yoshni Kiriting')
    await state.set_state(US.Yosh_k)


@dp.message(US.Yosh_k)
async def get_yosh(message: Message, state: FSMContext):
    yosh = message.text
    await state.update_data(yosh=yosh)
    await message.answer(text='Tilni Kiriting')
    await state.set_state(US.Til_k)


@dp.message(US.Til_k)
async def get_til(message: Message, state: FSMContext):
    til = message.text
    await state.update_data(til=til)
    await message.answer(text='Telefonni Kiriting')
    await state.set_state(US.Tel_k)


@dp.message(US.Tel_k)
async def get_tel(message: Message, state: FSMContext):
    telefon = message.text
    await state.update_data(telefon=telefon)
    await message.answer(text='Viloyatingizni Kiriting')
    await state.set_state(US.Vil_k)


@dp.message(US.Vil_k)
async def get_viloyat(message: Message, state: FSMContext):
    viloyat = message.text
    await state.update_data(viloyat=viloyat)
    user_data = await state.get_data()
    ism = user_data.get('ism')
    yosh = user_data.get('yosh')
    til = user_data.get('til')
    telefon = user_data.get('telefon')
    viloyat = user_data.get('viloyat')

    await message.answer(text=f"Ismingiz: {ism}\nYoshingiz: {yosh}\nTil: {til}\nTelefon: {telefon}\nViloyat: {viloyat}")
    await state.clear()

@dp.message(F.text == 'SHerik Kerak')
async def start_ism(message: Message, state: FSMContext):
    await state.set_state(US.ism_k)
    await message.answer(text='Ismni Kiriting')


@dp.message(SHeK.ism_y)
async def get_ism(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await message.answer(text='Yoshni Kiriting')
    await state.set_state(SHeK.Yosh_y)


@dp.message(SHeK.Yosh_y)
async def get_yosh(message: Message, state: FSMContext):
    yosh = message.text
    await state.update_data(yosh=yosh)
    await message.answer(text='Tilni Kiriting')
    await state.set_state(SHeK.Til_y)


@dp.message(SHeK.Til_y)
async def get_til(message: Message, state: FSMContext):
    til = message.text
    await state.update_data(til=til)
    await message.answer(text='Telefonni Kiriting')
    await state.set_state(SHeK.Tel_y)


@dp.message(SHeK.Tel_y)
async def get_tel(message: Message, state: FSMContext):
    telefon = message.text
    await state.update_data(telefon=telefon)
    await message.answer(text='Viloyatingizni Kiriting')
    await state.set_state(SHeK.Vil_y)


@dp.message(SHeK.Vil_y)
async def get_viloyat(message: Message, state: FSMContext):
    viloyat = message.text
    await state.update_data(viloyat=viloyat)
    user_data = await state.get_data()
    ism = user_data.get('ism')
    yosh = user_data.get('yosh')
    til = user_data.get('til')
    telefon = user_data.get('telefon')
    viloyat = user_data.get('viloyat')

    await message.answer(text=f"Ismingiz: {ism}\nYoshingiz: {yosh}\nTil: {til}\nTelefon: {telefon}\nViloyat: {viloyat}")
    await state.clear()



@dp.message(F.text == 'Hodim Kerak')
async def start_ism(message: Message, state: FSMContext):
    await state.set_state(US.ism_k)
    await message.answer(text='Ismni Kiriting')


@dp.message(HK.ism_h)
async def get_ism(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await message.answer(text='Yoshni Kiriting')
    await state.set_state(HK.Yosh_h)


@dp.message(HK.Yosh_h)
async def get_yosh(message: Message, state: FSMContext):
    yosh = message.text
    await state.update_data(yosh=yosh)
    await message.answer(text='Tilni Kiriting')
    await state.set_state(HK.Til_h)


@dp.message(HK.Til_h)
async def get_til(message: Message, state: FSMContext):
    til = message.text
    await state.update_data(til=til)
    await message.answer(text='Telefonni Kiriting')
    await state.set_state(HK.Tel_h)


@dp.message(HK.Tel_h)
async def get_tel(message: Message, state: FSMContext):
    telefon = message.text
    await state.update_data(telefon=telefon)
    await message.answer(text='Viloyatingizni Kiriting')
    await state.set_state(HK.Vil_h)


@dp.message(HK.Vil_h)
async def get_viloyat(message: Message, state: FSMContext):
    viloyat = message.text
    await state.update_data(viloyat=viloyat)
    user_data = await state.get_data()
    ism = user_data.get('ism')
    yosh = user_data.get('yosh')
    til = user_data.get('til')
    telefon = user_data.get('telefon')
    viloyat = user_data.get('viloyat')

    await message.answer(text=f"Ismingiz: {ism}\nYoshingiz: {yosh}\nTil: {til}\nTelefon: {telefon}\nViloyat: {viloyat}")
    await state.clear()


@dp.message(F.text == 'Ustoz Kerak')
async def start_ism(message: Message, state: FSMContext):
    await state.set_state(UK.ism_u)
    await message.answer(text='Ismni Kiriting')


@dp.message(UK.ism_u)
async def get_ism(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await message.answer(text='Yoshni Kiriting')
    await state.set_state(UK.Yosh_u)


@dp.message(UK.Yosh_u)
async def get_yosh(message: Message, state: FSMContext):
    yosh = message.text
    await state.update_data(yosh=yosh)
    await message.answer(text='Tilni Kiriting')
    await state.set_state(UK.Til_u)


@dp.message(UK.Til_u)
async def get_til(message: Message, state: FSMContext):
    til = message.text
    await state.update_data(til=til)
    await message.answer(text='Telefonni Kiriting')
    await state.set_state(UK.Tel_u)


@dp.message(UK.Tel_u)
async def get_tel(message: Message, state: FSMContext):
    telefon = message.text
    await state.update_data(telefon=telefon)
    await message.answer(text='Viloyatingizni Kiriting')
    await state.set_state(UK.Vil_u)


@dp.message(UK.Vil_u)
async def get_viloyat(message: Message, state: FSMContext):
    viloyat = message.text
    await state.update_data(viloyat=viloyat)
    user_data = await state.get_data()
    ism = user_data.get('ism')
    yosh = user_data.get('yosh')
    til = user_data.get('til')
    telefon = user_data.get('telefon')
    viloyat = user_data.get('viloyat')

    await message.answer(text=f"Ismingiz: {ism}\nYoshingiz: {yosh}\nTil: {til}\nTelefon: {telefon}\nViloyat: {viloyat}")
    await state.clear()




@dp.message(F.text == 'SHogirt Kerak')
async def start_ism(message: Message, state: FSMContext):
    await state.set_state(UK.ism_u)
    await message.answer(text='Ismni Kiriting')


@dp.message(SHK.ism_sh)
async def get_ism(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await message.answer(text='Yoshni Kiriting')
    await state.set_state(SHK.Yosh_sh)


@dp.message(SHK.Yosh_sh)
async def get_yosh(message: Message, state: FSMContext):
    yosh = message.text
    await state.update_data(yosh=yosh)
    await message.answer(text='Tilni Kiriting')
    await state.set_state(SHK.Til_sh)


@dp.message(SHK.Til_sh)
async def get_til(message: Message, state: FSMContext):
    til = message.text
    await state.update_data(til=til)
    await message.answer(text='Telefonni Kiriting')
    await state.set_state(SHK.Tel_sh)


@dp.message(SHK.Tel_sh)
async def get_tel(message: Message, state: FSMContext):
    telefon = message.text
    await state.update_data(telefon=telefon)
    await message.answer(text='Viloyatingizni Kiriting')
    await state.set_state(SHK.Vil_sh)


@dp.message(SHK.Vil_sh)
async def get_viloyat(message: Message, state: FSMContext):
    viloyat = message.text
    await state.update_data(viloyat=viloyat)
    user_data = await state.get_data()
    ism = user_data.get('ism')
    yosh = user_data.get('yosh')
    til = user_data.get('til')
    telefon = user_data.get('telefon')
    viloyat = user_data.get('viloyat')

    await message.answer(text=f"Ismingiz: {ism}\nYoshingiz: {yosh}\nTil: {til}\nTelefon: {telefon}\nViloyat: {viloyat}")
    await state.clear()




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except Exception as e:
        print(f"Xatolik: {e}")