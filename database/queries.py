create_films_table= """
    CREATE TABLE IF NOT EXISTS films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    film_id INTEGER NOT NULL
    )
"""
create_film_detail_table = """
    CREATE TABLE IF NOT EXISTS film_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT, 
    rating INTEGER,
    film_id INTEGER NOT NULL)"""

insert_film = 'INSERT INTO films(title, film_id) VALUES(?, ?)'
insert_film_detail = 'INSERT INTO film_detail(genre, rating, film_id) VALUES(?, ?, ?)'












create_products_table = """ 
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER,
    product_id INTEGER NOT NULL
    
); """


create_products_detail_table = """
    CREATE TABLE IF NOT EXISTS product_detail (
    description TEXT,
    product_id INTEGER NOT NULL,
    category TEXT
    )
"""

select_all_products= "SELECT * FROM  products;"

insert_product= 'INSERT INTO products(name, price, product_id ) VALUES (?, ?, ?)'
insert_product_detail= 'INSERT INTO product_detail (description, product_id, category) VALUES (?, ?, ?)'