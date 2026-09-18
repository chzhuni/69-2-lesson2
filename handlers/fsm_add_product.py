from aiogram import Router, F 
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import add_product_db

class AddProduct(StatesGroup):
    name = State()
    price = State()
    description = State()
    product_id = State()
    category = State()
    

router_addproduct= Router()
@router_addproduct.message(Command('cancel'))
async def cancel_handler_fsm(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета отменена.")
@router_addproduct.message(Command('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите название товавра: ')
    await state.set_state(AddProduct.name)

@router_addproduct.message(AddProduct.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену товара: ')
    await state.set_state(AddProduct.price)

@router_addproduct.message(AddProduct.price)
async def add_price(message: Message, state: FSMContext):
    if not message.text.isdigit():
            await message.answer('Пожалуйста, введите цену числом!')
            return
    await state.update_data(price=message.text)
    await message.answer('Напишите описание товара: ')
    await state.set_state(AddProduct.description)

@router_addproduct.message(AddProduct.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Напишите артикул товара: ')
    await state.set_state(AddProduct.product_id)

@router_addproduct.message(AddProduct.product_id)
async def add_product_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
            await message.answer('Пожалуйста, введите цену числом!')
            return
    await state.update_data(product_id=message.text)
    await message.answer('Напишите категорию товара: ')
    await state.set_state(AddProduct.category)

@router_addproduct.message(AddProduct.category)
async def add_categoty(message: Message, state: FSMContext):
    data= await state.update_data(category=message.text)

    await message.answer(f"Данные товара:\nНазвание — {data['name']}\nЦена — {data['price']}\nОписание —  {data['description']}\nАртикул — {data['product_id']}\nКатегория — {data['category']}") 

    await add_product_db(name=data['name'],
                         price=data['price'], 
                         description=data['description'], 
                         product_id=data['product_id'], 
                         category=data['category']
                         )
    await state.clear()