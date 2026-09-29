"""A bounded login-attempt loop."""


def check_pin(expected_pin: str = "2468", attempts: int = 3) -> bool:
    for remaining in range(attempts, 0, -1):
        entered = input("PIN: ")
        if entered == expected_pin:
            print("Access granted")
            return True
        print(f"Incorrect. {remaining - 1} attempt(s) left.")
    print("Account locked")
    return False


if __name__ == "__main__":
    check_pin()

