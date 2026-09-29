"""Simple educational validators; production uses Pydantic later."""


def is_valid_email(value: str) -> bool:
    value = value.strip()
    if value.count("@") != 1:
        return False
    local, domain = value.split("@")
    return bool(local and "." in domain and not domain.startswith("."))


def is_non_empty(value: str) -> bool:
    return bool(value.strip())

