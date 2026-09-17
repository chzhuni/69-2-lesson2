create_products_table = """ 
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER,
    description TEXT
); """

insert_product= 'INSERT INTO products(name, price, description) VALUES (?, ?, ?)'

select_all_products= "SELECT * FROM  products;"