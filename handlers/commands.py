from aiogram import  F, Router 
from aiogram.filters import Command 
from aiogram.types import Message 
from config import bot
import random
from datetime import datetime
from database.db import get_all_products_db

router_commands = Router()

@router_commands.message(Command("start")) 
async def start_handler(message: Message):
     await message.answer(f"Привет! Я личный бот Николь.\n/help — список команд\nТвой ID {message.from_user.id}")

@router_commands.message(Command("help"))
async def help_handler(message: Message): 
    await message.answer(
         "Доступные команды:\n"
          "/start — начать\n" 
          "/help — список команд\n" 
          "/time — текущая дата\n" 
          "/random — выдает рандомное число\n" 
          "/joke — рассказывает шутку\n"
          "/add_product  — добавляет товар\n"
          "/add_film  — добавляет фильм\n"
        )

@router_commands.message(F.text == 'Привет')
async def hello_text_handler(message: Message):
    await message.answer('Привет!!')

@router_commands.message(Command('time'))
async def time_handler(message: Message):
    now = datetime.now()
    form = now.strftime('%d.%m.%Y %H:%M')
    await message.answer(f'Сейчас: {form}')

@router_commands.message(Command('random'))
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


@router_commands.message(Command('all_products'))
async def all_products_handler(message: Message):
    products= await get_all_products_db()
    result = ""
    for product in products:
        result = result + f'{product[1]}, {product[2]} сом, {product[3]}\n'
    await message.answer(result)
 
@router_commands.message(Command('joke'))
async def joke_handler(message: Message):
    joke = random.choice(jokes)
    await message.answer(joke)