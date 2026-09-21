import aiosqlite
path_db = 'database/bot.db'
from database.queries import (
    create_products_table, 
    create_products_detail_table, 
    select_all_products, 
    insert_product, 
    insert_product_detail,
    create_films_table, 
    create_film_detail_table,
    insert_film, 
    insert_film_detail
) 

async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(create_products_table)
        await conn.execute(create_products_detail_table)
        await conn.execute(create_films_table)
        await conn.execute(create_film_detail_table)
        await conn.commit()
    print('database connect')

async def add_film_db(title, film_id, genre, rating):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(insert_film, (title, film_id))
        await conn.execute(insert_film_detail, (genre, rating, film_id))
        await conn.commit()

async def add_product_db(name, price, description, product_id, category):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(insert_product, (name, price, product_id))
        await conn.execute(insert_product_detail, (description, product_id, category))
        await conn.commit()

async def get_all_products_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(select_all_products)
        rows = await cursor.fetchall()
    return rows

# """SQLite3 DATA BASE"""
# import sqlite3.
# path_db = 'database/sqlite3.db'

# def init_db():
#     conn = sqlite3.connect(database=path_db)
#     cursor = conn.cursor()
#     print('БД подключена')
#     cursor.execute(create_products_table)
#     conn.commit()
#     conn.close()

# def add_product_db(name, price, description):
#     conn=sqlite3.connect(database=path_db)
#     cursor = conn.cursor()
#     cursor.execute(insert_product, (name, price, description))
#     conn.commit()
#     conn.close()

# def get_all_products_db():
#     conn = sqlite3.connect(database=path_db)
#     cursor = conn.cursor()
#     cursor.execute(select_all_products)
#     rows = cursor.fetchall()
#     conn.close()
#     return rows