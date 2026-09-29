from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import format_employee, is_valid_email  # noqa: E402

record = {"id": "E-100", "name": input("Name: ").strip(), "active": True}
email = input("Email: ").strip()
print(format_employee(record) if is_valid_email(email) else "Invalid email")

