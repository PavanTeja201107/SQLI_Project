import sqlite3
import time

def safe_query(user_id):

    start = time.perf_counter()

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id=?"

    cursor.execute(query,(user_id,))

    data = cursor.fetchall()

    conn.close()

    end = time.perf_counter()

    runtime = end - start

    return data, runtime