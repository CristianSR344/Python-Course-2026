"""Persistent JSON user manager solution."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("managed_users.json")


def load_users() -> list[dict[str, object]]:
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        print(f"Invalid data file: {error}")
        return []


def save_users(users: list[dict[str, object]]) -> None:
    DATA_FILE.write_text(json.dumps(users, indent=2), encoding="utf-8")


def main() -> None:
    users = load_users()
    while True:
        choice = input("1 Add | 2 List | 3 Search | 4 Delete | 5 Quit: ").strip()
        if choice == "1":
            users.append({"id": max((int(u["id"]) for u in users), default=0) + 1,
                          "name": input("Name: ").strip()})
            save_users(users)
        elif choice == "2":
            print(*users, sep="\n")
        elif choice == "3":
            query = input("Name: ").lower()
            print(*[u for u in users if query in str(u["name"]).lower()], sep="\n")
        elif choice == "4":
            user_id = int(input("ID: "))
            users[:] = [u for u in users if u["id"] != user_id]
            save_users(users)
        elif choice == "5":
            break


if __name__ == "__main__":
    main()

