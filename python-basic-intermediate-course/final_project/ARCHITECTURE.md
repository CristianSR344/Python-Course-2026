# Architecture

```text
Browser / API client
        ↓
FastAPI routers (HTTP, forms, templates)
        ↓
UserService (workflow and email composition)
       ↙ ↘
UserRepository   EmailService
       ↓              ↓
SQLAlchemy/SQLite  SMTP or logs/emails
```

The service receives its collaborators in `__init__`. This is composition: it *uses* a repository and email service rather than inheriting from them. Encapsulation keeps SQL and SMTP details behind focused methods. Tests can substitute a temporary database and log directory without changing business code.

