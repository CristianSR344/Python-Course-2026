# User Management & Notification Portal

A teaching application that connects fundamentals to a realistic architecture: FastAPI routers call a `UserService`; the service composes `UserRepository` and `EmailService`; the repository alone talks to SQLAlchemy/SQLite.

## Run

From this directory, after installing requirements:

```powershell
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000`, JSON documentation at `/docs`, and run tests with `pytest`. The SQLite database is created in `data/app.db`. Without complete SMTP settings, welcome messages are saved under `logs/emails`.

For class use, trace one request from `routers/users.py` through the service and repository. See `PROJECT_REQUIREMENTS.md` and `ARCHITECTURE.md`.

