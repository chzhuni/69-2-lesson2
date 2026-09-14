from aiogram import Router, F 
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class AddFilm(StatesGroup):
    title = State()
    genre = State()
    rating = State()

router_addfilm = Router()
@router_addfilm.message(Command('cancel'))
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета отменена.")

@router_addfilm.message(Command('add_film'))
async def add_fsm_start(message: Message, state: FSMContext):
    await message.answer('Введите название фильма: ')
    await state.set_state(AddFilm.title)

@router_addfilm.message(AddFilm.title)
async def add_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer('Введите жанр фильма: ')
    await state.set_state(AddFilm.genre)

@router_addfilm.message(AddFilm.genre)
async def add_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer('Введите рейтинг: ')
    await state.set_state(AddFilm.rating)

@router_addfilm.message(AddFilm.rating)
async def add_rating(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите в рейтинг ЧИСЛО!!")
        return
    data = await state.update_data(rating=message.text)

    await message.answer(f"Данные фильма:\nНазвание — {data['title']}\nЖанр — {data['genre']}\nРейтинг — {data['rating']}")
    await state.clear()