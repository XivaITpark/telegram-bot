import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from transliterate import to_cyrillic,to_latin


bot = Bot(token="7708717823:AAFlHx_eBHfDl_maMLa3ZuBfKz4pfkxbF7Y")
dp=Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Krill va Lotn botga hush kelibsiz")


@dp.message()
async def cmd_start(message:types.Message):
    matin = message.text
    if matin.isascii():
        await message.reply(to_cyrillic(matin))
    else:
        await message.reply(to_latin(matin))





async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())