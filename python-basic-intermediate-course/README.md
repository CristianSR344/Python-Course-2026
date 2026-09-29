# Python Basic–Intermediate Course

An instructor-ready, six-session course for beginners. It progresses from variables and control flow through data structures, functions, files, OOP, SQLite, and a complete FastAPI user-management portal.

## Prerequisites and outcomes

Install Python 3.11+ and a code editor. No programming experience is required. By completion, students can write modular Python, validate data, persist it in JSON/SQLite, model domains with classes, and build/test CRUD web applications.

## Quick start

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
jupyter notebook
```

On macOS/Linux activate with `source .venv/bin/activate`. Run examples from the repository root with `python path/to/file.py`.

## Course sequence

1. `00_setup` and `01_fundamentals`: tools, values, input, and expressions.
2. `02_control_flow`: decisions, validation, and repetition.
3. `03_data_structures`: collections and a contact manager.
4. `04_functions_modules` and `05_files_errors_json`: reusable, persistent programs.
5. `06_oop`: classes and an OOP ticket system.
6. `07_web_api_intro`, `08_database`, and `final_project`: HTTP, validation, CRUD, SQLite, templates, and email.

Exercises are kept beside each lesson; completed versions are in that lesson's `solutions` directory. Session quizzes live in `assessments`, and reference sheets in `resources`.

Detailed PDF walkthroughs and trainer key points for every module are in `trainer_guides`. Regenerate them with `python tools/build_module_pdfs.py`.

## Final project

The User Management & Notification Portal provides HTML and JSON interfaces for creating, searching, viewing, editing, and deleting users. It uses FastAPI, Pydantic, SQLAlchemy, SQLite, Jinja2, and a safe file-based email fallback.

```powershell
cd final_project
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000>; interactive API documentation is at <http://127.0.0.1:8000/docs>.

See `COURSE_GUIDE.md` for the learning path, `STUDENT_GUIDE.md` for detailed setup, and `INSTRUCTOR_GUIDE.md` for delivery notes.
