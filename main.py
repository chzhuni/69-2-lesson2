import asyncio 
import logging
from datetime import datetime
import random

from aiogram import Bot, Dispatcher, F, Router 
from aiogram.filters import Command 
from aiogram.types import Message 
from decouple import config


TOKEN = config("BOT_TOKEN")
bot = Bot(token=TOKEN) 
dp = Dispatcher() 
router = Router()

@router.message(Command("start")) 
async def start_handler(message: Message):
     await message.answer("Привет! Я личный бот Николь.")

@router.message(Command("help"))
async def help_handler(message: Message): 
    await message.answer(
         "Доступные команды:\n"
          "/start — начать\n" 
          "/help — список команд\n" 
          "/time — текущая дата\n "
          "/random — выдает рандомное число\n"
          "/joke — рассказывает шутку "
        )

@router.message(F.text == 'Привет')
async def hello_text_handler(message: Message):
    await message.answer('Привет!!')

@router.message(Command('time'))
async def time_handler(message: Message):
    now = datetime.now()
    form = now.strftime('%d.%m.%Y %H:%M')
    await message.answer(f'Сейчас: {form}')

@router.message(Command('random'))
async def random_handler(message: Message):
    number = random.randint(1, 100)
    await message.answer(f'Рандомное число: {number}')

jokes = [
    ' — Почему компьютер пошёл к врачу? — Потому что у него был вирус.',
    ' — Что сказал ноль восьмёрке? — «Классный ремень!»',
    ' Я решил начать новую жизнь с понедельника. Понедельник посмотрел на меня и тоже решил не торопиться.',
    '— Ты почему опоздал в школу? — Я вышел вовремя, но дорога была против.',
    ' Купил умные часы. Теперь они каждый день напоминают мне, что я ничего не делаю. Кажется, умнее в этой покупке оказались часы.',
    ]

@router.message(Command('joke'))
async def joke_handler(message: Message):
    joke = random.choice(jokes)
    await message.answer(joke)

@router.message(F.text)
async def echo_handler(message: Message): 
    await message.answer(f"Такой команды нет: {message.text}")


async def main(): 
    dp.include_router(router) 
    await dp.start_polling(bot)

if __name__ == "__main__": 
    logging.basicConfig(level=logging.INFO) 
    asyncio.run(main())
