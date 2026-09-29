"""Notification inheritance and polymorphism example."""


class Notification:
    def __init__(self, recipient: str, message: str):
        self.recipient = recipient
        self.message = message

    def send(self) -> str:
        raise NotImplementedError("Subclasses choose a delivery method")


class EmailNotification(Notification):
    def send(self) -> str:
        return f"Email to {self.recipient}: {self.message}"

