class User:
    def __init__(self, name: str, email: str, active: bool = True):
        self.name, self.email, self.active = name, email, active

    def deactivate(self) -> None:
        self.active = False

    def __str__(self) -> str:
        return f"{self.name} <{self.email}> active={self.active}"

