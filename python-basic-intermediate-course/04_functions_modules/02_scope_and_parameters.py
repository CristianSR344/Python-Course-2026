"""Parameters, keyword arguments, defaults, and local scope."""

DEFAULT_DOMAIN = "example.org"


def create_email(first_name: str, last_name: str, domain: str = DEFAULT_DOMAIN) -> str:
    local_part = f"{first_name}.{last_name}".strip(".").lower().replace(" ", "")
    return f"{local_part}@{domain}"


if __name__ == "__main__":
    print(create_email("Ada", "Lovelace"))
    print(create_email(last_name="Hopper", first_name="Grace", domain="navy.mil"))

