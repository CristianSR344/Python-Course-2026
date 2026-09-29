import sqlite3


def update(database: sqlite3.Connection, user_id: int, name: str) -> bool:
    return database.execute("UPDATE users SET name=? WHERE id=?", (name, user_id)).rowcount > 0


def delete(database: sqlite3.Connection, user_id: int) -> bool:
    return database.execute("DELETE FROM users WHERE id=?", (user_id,)).rowcount > 0

