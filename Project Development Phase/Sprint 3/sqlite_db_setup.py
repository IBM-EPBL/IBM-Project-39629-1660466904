import sqlite3

conn = sqlite3.connect('ntapp.db')
print("Opened database successfully")

conn.execute('CREATE TABLE user_login (email TEXT, password TEXT, name TEXT)')
conn.execute('CREATE TABLE user_data (email TEXT, choices TEXT)')
print("Table created successfully")
conn.close()