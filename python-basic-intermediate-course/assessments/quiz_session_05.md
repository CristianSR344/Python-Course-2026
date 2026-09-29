# Session 5 Quiz — OOP

## Multiple choice

1. What creates instance state? A) __init__ B) __str__ C) import D) except
2. The current instance parameter is conventionally: A) this B) self C) cls only D) object
3. `Employee(User)` demonstrates: A) composition B) inheritance C) JSON D) iteration
4. A service receiving a repository demonstrates: A) slicing B) composition C) conversion D) looping
5. What provides readable object text? A) __str__ B) __init__ C) property only D) super only

## Read code

6. What changes? `user.active=True; user.deactivate()` sets `self.active=False`.
7. Why might `EmailNotification.send` override `Notification.send`?

## Write code

8. Define a Ticket with title and open status.
9. Define `Employee(User)` and call `super().__init__`.

## Debug

10. Fix: `class User: def __init__(name): self.name = name`.

<details><summary>Instructor answers</summary>

1 A; 2 B; 3 B; 4 B; 5 A. 6: active becomes False. 7: polymorphic delivery behavior. 8: initialize `self.title` and `self.status="open"`. 9: subclass and initialize parent before employee fields. 10: signature must be `def __init__(self, name)`.
</details>

