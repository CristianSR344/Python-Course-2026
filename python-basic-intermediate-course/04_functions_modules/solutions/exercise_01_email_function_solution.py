def is_valid_email(email: str) -> bool:
    parts = email.strip().split("@")
    return len(parts) == 2 and bool(parts[0]) and "." in parts[1]


print(is_valid_email("student@example.com"))

