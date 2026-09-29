"""Encapsulation through validated state changes."""


class Ticket:
    VALID_STATUSES = {"open", "assigned", "closed"}

    def __init__(self, title: str):
        self.title = title
        self._status = "open"

    @property
    def status(self) -> str:
        return self._status

    def change_status(self, new_status: str) -> None:
        if new_status not in self.VALID_STATUSES:
            raise ValueError(f"Status must be one of {sorted(self.VALID_STATUSES)}")
        self._status = new_status


if __name__ == "__main__":
    ticket = Ticket("Cannot sign in")
    ticket.change_status("assigned")
    print(ticket.title, ticket.status)

