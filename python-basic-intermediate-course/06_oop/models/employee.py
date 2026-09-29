from .user import User


class Employee(User):
    def __init__(self, user_id: int, name: str, email: str,
                 employee_id: str, department: str, active: bool = True):
        super().__init__(user_id, name, email, active)
        self.employee_id = employee_id.strip().upper()
        self.department = department.strip().title()

    def __str__(self) -> str:
        return f"{super().__str__()} | {self.employee_id} | {self.department}"

