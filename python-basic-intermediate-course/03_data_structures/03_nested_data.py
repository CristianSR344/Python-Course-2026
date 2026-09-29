"""Search and summarize a list of user dictionaries."""

USERS = [
    {"id": 1, "name": "Ana Cruz", "department": "Support", "active": True},
    {"id": 2, "name": "Ben Ito", "department": "Sales", "active": False},
    {"id": 3, "name": "Cara Fox", "department": "Support", "active": True},
]


def find_user(user_id: int) -> dict[str, object] | None:
    return next((user for user in USERS if user["id"] == user_id), None)


if __name__ == "__main__":
    active_names = [user["name"] for user in USERS if user["active"]]
    departments = {user["department"] for user in USERS}
    print("Active:", ", ".join(active_names))
    print("Departments:", sorted(departments))
    print("Found:", find_user(2))

