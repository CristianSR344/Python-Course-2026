"""Course User model."""


class User:
    organization = "Course Portal"

    def __init__(self, user_id: int, name: str, email: str, active: bool = True):
        self.user_id = user_id
        self.name = name.strip().title()
        self.email = email.strip().lower()
        self.active = active

    def deactivate(self) -> None:
        self.active = False

    def __str__(self) -> str:
        status = "active" if self.active else "inactive"
        return f"{self.user_id}: {self.name} <{self.email}> ({status})"

