def format_employee(name: str, department: str, active: bool = True) -> str:
    status = "Active" if active else "Inactive"
    return f"{name.strip().title()} — {department.strip().title()} ({status})"


print(format_employee("ada lovelace", "engineering"))

