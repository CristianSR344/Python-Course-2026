from pathlib import Path
import sqlite3

path = Path(__file__).with_name("exercise.db")
with sqlite3.connect(path) as database:
    database.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")
    database.execute("INSERT INTO users(name) VALUES (?)", ("Ada",))
    print(database.execute("SELECT * FROM users").fetchall())

