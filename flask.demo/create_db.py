import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("INSERT INTO users(username,password) VALUES('admin','admin123')")
cursor.execute("INSERT INTO users(username,password) VALUES('user','1234')")
cursor.execute("INSERT INTO users(username,password) VALUES('test','pass')")

conn.commit()

conn.close()

print("Database and users table created successfully")