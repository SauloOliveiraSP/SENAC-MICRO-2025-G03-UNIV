import sqlite3
import os

DB_NAME = "users.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_NAME):
        conn = get_db_connection()
        conn.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))
        conn.commit()
        conn.close()
