"""CRUD functions using parameterized SQL outside any web route."""

from database import connection, initialize


def create_user(name: str, email: str) -> int:
    with connection() as database:
        cursor = database.execute("INSERT INTO users(name, email) VALUES (?, ?)",
                                  (name, email))
        return int(cursor.lastrowid)


def list_users() -> list[dict[str, object]]:
    with connection() as database:
        return [dict(row) for row in database.execute("SELECT * FROM users ORDER BY id")]


def update_user(user_id: int, name: str, email: str) -> bool:
    with connection() as database:
        cursor = database.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        return cursor.rowcount > 0


def delete_user(user_id: int) -> bool:
    with connection() as database:
        cursor = database.execute("DELETE FROM users WHERE id = ?", (user_id,))
        return cursor.rowcount > 0


if __name__ == "__main__":
    initialize()
    print(list_users())

