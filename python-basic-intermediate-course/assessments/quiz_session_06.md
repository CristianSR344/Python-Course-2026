# Session 6 Quiz — Web, API, and Database

## Multiple choice

1. Which method normally creates? A) GET B) POST C) DELETE D) HEAD
2. Which status means Created? A) 200 B) 201 C) 204 D) 404
3. What validates request models? A) SQLite B) Pydantic C) CSS D) Jinja only
4. Which SQLite rule uniquely identifies a row? A) heading B) primary key C) route D) template
5. Where should SQL live in this project? A) template B) router C) repository D) CSS

## Read code

6. What response should a missing `/api/users/99` return?
7. Explain `UserService(UserRepository(session), EmailService(settings))`.

## Write code

8. Write a FastAPI health GET route returning `{"status":"ok"}`.
9. Write parameterized SQL to select a user by ID.

## Debug

10. Why can `uvicorn app.main:app` fail when run from the repository root, and how is it fixed?

<details><summary>Instructor answers</summary>

1 B; 2 B; 3 B; 4 B; 5 C. 6: 404. 7: composition/injection of persistence and email collaborators. 8: decorate a function with `@app.get("/health")`. 9: `execute("SELECT * FROM users WHERE id=?", (user_id,))`. 10: `app` is under `final_project`; change into that directory or use the appropriate module/app-dir path.
</details>

