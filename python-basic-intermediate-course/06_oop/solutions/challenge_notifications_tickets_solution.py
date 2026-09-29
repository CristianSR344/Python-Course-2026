from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from models.notification import EmailNotification  # noqa: E402
from models.user import User  # noqa: E402


class Ticket:
    def __init__(self, title: str):
        self.title, self.assignee, self.status = title, None, "open"

    def assign(self, user: User) -> str:
        self.assignee, self.status = user, "assigned"
        return EmailNotification(user.email, f"Assigned: {self.title}").send()


agent = User(1, "Ada", "ada@example.com")
print(Ticket("Login problem").assign(agent))

