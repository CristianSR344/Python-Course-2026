import json
from pathlib import Path

path = Path(__file__).with_name("users_solution.json")
users = [{"id": 1, "name": "Ana", "active": True}]
path.write_text(json.dumps(users, indent=2), encoding="utf-8")
try:
    print(json.loads(path.read_text(encoding="utf-8")))
except (FileNotFoundError, json.JSONDecodeError) as error:
    print(f"Could not load users: {error}")

