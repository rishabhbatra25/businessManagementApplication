import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS customers (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT,customer_address TEXT,customer_city TEXT,customer_state TEXT,
customer_mobile TEXT,customer_gst TEXT,customer_pan TEXT,customer_gst_type TEXT,customer_group TEXT)''')
con.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name TEXT, product_availablity TEXT DEFAULT 'Available', product_hsn TEXT,product_cgst NUMERIC,
product_sgst NUMERIC,product_igst NUMERIC,product_group TEXT)''')
con.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS suppliers (supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
supplier_name TEXT,supplier_address TEXT,supplier_city TEXT,supplier_state TEXT,supplier_mobile TEXT,
supplier_gst TEXT,supplier_pan TEXT,supplier_gst_type TEXT,supplier_group TEXT)''')
con.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS items (orderId INTEGER,products TEXT,customer_id INTEGER,
hsn TEXT,quantity REAL,net_rate REAL,rate REAL,	tax TEXT,total REAL,cgst REAL,sgst REAL,amount REAL,agent TEXT,
transport TEXT,payment_mode TEXT,date TEXT,discount REAL,total_cgst REAL,total_sgst REAL,total_amount REAL,
customer TEXT)''')
con.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS orders (orderId INTEGER PRIMARY KEY AUTOINCREMENT,
customer_id INTEGER,date TEXT,total_amount REAL)''')
con.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS purchase (billnoId INTEGER,products TEXT,supplier_id INTEGER,
hsn TEXT,quantity REAL,net_rate REAL,rate REAL,tax TEXT,total REAL,cgst TEXT,sgst REAL,amount REAL,agent TEXT,
transport TEXT,payment_mode TEXT,date TEXT,discount REAL DEFAULT 0,total_cgst REAL,total_sgst REAL,
total_amount REAL,supplier TEXT,stock REAL DEFAULT 0)''')
con.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS stock (product_id INTEGER,product TEXT,stock REAL DEFAULT 0)''')
con.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS bills (billnoId INTEGER PRIMARY KEY AUTOINCREMENT,supplier_id INTEGER,
date TEXT)''')
con.commit()



