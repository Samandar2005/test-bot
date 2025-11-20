import sqlite3
from contextlib import closing

DB_FILE = "users.db"


def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY
            )
            """
        )


def add_user(user_id: int):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO users (id) VALUES (?)",
            (user_id,),
        )
        conn.commit()


def load_users():
    with sqlite3.connect(DB_FILE) as conn, closing(conn.cursor()) as cur:
        cur.execute("SELECT id FROM users")
        return [row[0] for row in cur.fetchall()]


# Ensure table exists on import
init_db()
