"""Input/output demonstration and registration summary."""


def registration_summary(name: str, email: str, department: str, age: int) -> str:
    return (
        "\n--- Registration Summary ---\n"
        f"Name: {name.strip().title()}\nEmail: {email.strip().lower()}\n"
        f"Department: {department.strip().title()}\nAge: {age}"
    )


def main() -> None:
    name = input("Name: ")
    email = input("Email: ")
    department = input("Department: ")
    age = int(input("Age: "))
    print(registration_summary(name, email, department, age))


if __name__ == "__main__":
    main()

