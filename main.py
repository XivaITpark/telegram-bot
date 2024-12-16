import asyncio

from button import qwerty
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import wikipedia
wikipedia.set_lang("uz")


bot=Bot(token="7995710856:AAGv9HHcGMJkPBlKqjgX9PNnejG_qYF8S4E")
dp=Dispatcher()

@dp.message(Command("start"))
async def start(message:Message):
    await message.answer("Salom botga hush kelibsiz. Bu bot siz hohlagan malumotni olib korsatadi!",reply_markup=qwerty)

@dp.message(F.text=="O'zbekiston")
async def echo(message:Message):
    reply=wikipedia.summary(message.text)
    await message.answer(reply,reply_markup=qwerty)

@dp.message(F.text == 'Xorazm')
async def echo(message:Message):
        reply = wikipedia.summary(message.text)
        await message.answer(reply, reply_markup=qwerty)



@dp.message(F.text=='BMW')
async def echo(message:Message):
    reply=wikipedia.summary(message.text)
    await message.answer(reply,reply_markup=qwerty)

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run((main()))