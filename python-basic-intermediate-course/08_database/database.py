"""Reusable standard-library SQLite connection for lesson exercises."""

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent / "course_users.db"


@contextmanager
def connection(path: Path = DATABASE_PATH) -> Iterator[sqlite3.Connection]:
    database = sqlite3.connect(path)
    database.row_factory = sqlite3.Row
    try:
        yield database
        database.commit()
    except Exception:
        database.rollback()
        raise
    finally:
        database.close()


def initialize(path: Path = DATABASE_PATH) -> None:
    with connection(path) as database:
        database.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)"
        )


if __name__ == "__main__":
    initialize()
    print(f"Initialized {DATABASE_PATH}")

