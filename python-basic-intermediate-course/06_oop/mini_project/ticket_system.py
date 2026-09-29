"""Object-oriented support ticket manager."""

from dataclasses import dataclass


class Notification:
    def send(self, recipient: str, message: str) -> str:
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"EMAIL {recipient}: {message}"


@dataclass
class Agent:
    name: str
    email: str


class Ticket:
    next_id = 1

    def __init__(self, title: str, description: str):
        self.id = Ticket.next_id
        Ticket.next_id += 1
        self.title, self.description = title, description
        self.status, self.assignee = "open", None

    def assign(self, agent: Agent) -> None:
        self.assignee, self.status = agent, "assigned"

    def close(self) -> None:
        self.status = "closed"

    def __str__(self) -> str:
        owner = self.assignee.name if self.assignee else "unassigned"
        return f"#{self.id} [{self.status}] {self.title} — {owner}"


class TicketManager:
    def __init__(self, notifier: Notification):
        self._tickets: list[Ticket] = []
        self._notifier = notifier

    def create(self, title: str, description: str) -> Ticket:
        ticket = Ticket(title, description)
        self._tickets.append(ticket)
        return ticket

    def assign(self, ticket: Ticket, agent: Agent) -> None:
        ticket.assign(agent)
        print(self._notifier.send(agent.email, f"Ticket #{ticket.id} assigned"))

    def list_all(self) -> list[Ticket]:
        return list(self._tickets)


if __name__ == "__main__":
    manager = TicketManager(EmailNotification())
    issue = manager.create("Cannot log in", "Password reset fails")
    manager.assign(issue, Agent("Ada", "ada@example.com"))
    print(*manager.list_all(), sep="\n")

