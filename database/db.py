import sqlite3
from database.queries import create_products_table, insert_product, select_all_products


path_db = 'database/sqlite3.db'

def init_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    print('БД подключена')
    cursor.execute(create_products_table)
    conn.commit()
    conn.close()

def add_product_db(name, price, description):
    conn=sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(insert_product, (name, price, description))
    conn.commit()
    conn.close()

def get_all_products_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(select_all_products)
    rows = cursor.fetchall()
    conn.close()
    return rows