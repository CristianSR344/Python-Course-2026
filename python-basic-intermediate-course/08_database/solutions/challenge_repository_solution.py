import sqlite3


class UserRepository:
    def __init__(self, database: sqlite3.Connection):
        self.database = database

    def create(self, name: str) -> int:
        cursor = self.database.execute("INSERT INTO users(name) VALUES (?)", (name,))
        self.database.commit()
        return int(cursor.lastrowid)

    def list_all(self) -> list[tuple]:
        return self.database.execute("SELECT * FROM users").fetchall()

