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
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                cpf TEXT NOT NULL,
                cep TEXT NOT NULL
            )
        """)
        conn.execute(
            "INSERT INTO users (username, password, email, cpf, cep) VALUES (?, ?, ?, ?, ?)", 
            ("admin", "1234", "admin@example.com", "000.000.000-00", "00000-000")
        )
        conn.commit()
        conn.close()
