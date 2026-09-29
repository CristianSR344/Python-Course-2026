class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name


class Employee(User):
    def __init__(self, name: str, department: str):
        super().__init__(name)
        self.department = department

    def __str__(self) -> str:
        return f"{super().__str__()} — {self.department}"

