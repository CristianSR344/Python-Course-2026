# Python Cheat Sheet

```python
# Values and conversion
name = "Ada"; age = int("36"); active = True; manager = None
print(f"{name}: {age}")

# Conditions and loops
if active and age >= 18:
    print("accepted")
for index, value in enumerate(["a", "b"], 1):
    print(index, value)

# Collections
items = [1, 2]; point = (4, 5); unique = {"IT", "HR"}
user = {"id": 1, "name": "Ada"}
found = next((u for u in [user] if u["id"] == 1), None)

# Functions/errors/files
def label(value: str, prefix: str = "User") -> str:
    return f"{prefix}: {value}"
try:
    number = int("x")
except ValueError as error:
    print(error)

from pathlib import Path
path = Path(__file__).with_name("data.txt")
path.write_text("hello", encoding="utf-8")
```

Use four-space indentation, descriptive `snake_case`, specific exceptions, and `if __name__ == "__main__":` for executable scripts.

