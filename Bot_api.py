from Config import Config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio


bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['not_sleep'])
async def not_sleep(message: types.Message):
    await message.answer(Config.Users[message.text[11:]][0])
    await asyncio.sleep(5)
    await message.answer(Config.Users[message.text[11:]][1])


if __name__ == "__main__":
    executor.start_polling(dp)