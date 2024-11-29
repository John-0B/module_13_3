from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['привет', 'Привет'])
async def hi(message):
    print('привет')
    await message.answer('Привет')


@dp.message_handler(commands=['старт'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print(message.text)
    await message.answer(f'Это я тебе говорю {message.text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)