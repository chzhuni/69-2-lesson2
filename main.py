import asyncio 
import logging
from config import dp, bot, Admin
from handlers import commands, echo, fsm_add_product, fsm_add_film
from aiogram.types import BotCommand
from database import db

async def set_commands():
    commands = [
        BotCommand(command='start', description='Старт бота'),
        BotCommand(command='help', description='helper'),
        BotCommand(command='time', description='текущая дата'),
        BotCommand(command='random', description='рандомное число'),
        BotCommand(command='joke', description='рассказывает шутку'),
        BotCommand(command='add_product', description='добавляет товар'),
        BotCommand(command='add_film', description='добавляет фильм'),
        BotCommand(command='cancel', description='отменяет заполнение анкеты'),
    ]
    await bot.set_my_commands(commands)

async def on_startup():
    await set_commands()
    for admin_id in Admin:
        await bot.send_message(chat_id=admin_id, text='Бот включен!')


async def main():
    dp.include_router(router=commands.router_commands)
    dp.include_router(router=fsm_add_product.router_addproduct)
    dp.include_router(router=fsm_add_film.router_addfilm)
    dp.include_router(router=echo.router_echo)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)



if __name__ == "__main__": 
    db.init_db()
    logging.basicConfig(level=logging.INFO) 
    asyncio.run(main())