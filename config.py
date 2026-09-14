from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("BOT_TOKEN")
Admin = [8776992906, ]

bot = Bot(token=TOKEN) 
dp = Dispatcher() 