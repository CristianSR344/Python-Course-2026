# Python Basic–Intermediate Course — Codex CLI Build Specification

## 1. Project Goal

Create a complete, instructor-ready Python course that teaches programming from basic syntax through Object-Oriented Programming (OOP), using progressive exercises, Jupyter notebooks, Python scripts, mini-projects, and one integrated final project.

The repository must be usable for a live instructor-led course and also for self-study.

The generated course must include:

- `.py` files for executable examples, exercises, utilities, and projects.
- `.ipynb` notebooks for explanations, guided demonstrations, interactive exercises, and visual examples.
- Markdown documentation for instructors and students.
- Solutions separated from student exercises.
- A cumulative final project built with FastAPI.
- SQLite persistence.
- HTML/CSS frontend templates.
- Email functionality.
- CRUD operations.
- Input validation.
- Object-Oriented Programming.
- Modular code organization.
- Basic automated tests.
- Clear setup instructions.

The course should prioritize practical programming over excessive theory.

---

## 2. Target Audience

Students with little or no Python programming experience.

By the end of the course, students should be able to:

1. Understand Python syntax and execution.
2. Work with variables and data types.
3. Use operators and expressions.
4. Create conditional logic.
5. Use `for` and `while` loops.
6. Work with lists, tuples, sets, and dictionaries.
7. Create reusable functions.
8. Handle exceptions.
9. Read and write files.
10. Organize Python programs into modules.
11. Use third-party libraries.
12. Understand classes and objects.
13. Apply encapsulation, inheritance, and composition.
14. Work with JSON and basic APIs.
15. Persist information in SQLite.
16. Build a small web application using FastAPI.
17. Implement CRUD operations.
18. Validate data with Pydantic.
19. Send emails from a Python application.
20. Organize a realistic Python project.

---

## 3. Course Duration

Design the course for:

- 6 sessions
- 2 hours per session
- 12 instructional hours total

Each session should approximately contain:

- 25–35 minutes: explanation and guided examples
- 30–40 minutes: coding exercises
- 30–40 minutes: cumulative mini-project
- 10–15 minutes: review, challenge, or quiz

Do not make each lesson purely theoretical.

Every session must produce code that contributes directly or conceptually to the final project.

---

## 4. Pedagogical Approach

Use progressive complexity.

Each topic must follow this pattern:

1. Explain the concept briefly.
2. Show a simple example.
3. Show a realistic example.
4. Give a guided exercise.
5. Give an independent challenge.
6. Include a solution in a separate location.
7. Connect the concept to the final project.

Avoid unnecessarily advanced abstractions before students understand the fundamentals.

Use meaningful examples such as:

- employee records
- user registrations
- inventories
- support tickets
- email notifications
- administrative dashboards
- task tracking
- CSV reports
- API requests

Avoid relying mainly on mathematical exercises.

---

## 5. Repository Structure

Generate the following repository structure:

```text
python-basic-intermediate-course/
│
├── README.md
├── COURSE_GUIDE.md
├── INSTRUCTOR_GUIDE.md
├── STUDENT_GUIDE.md
├── requirements.txt
├── .gitignore
│
├── 00_setup/
│   ├── README.md
│   ├── environment_check.py
│   └── 00_python_setup.ipynb
│
├── 01_fundamentals/
│   ├── README.md
│   ├── 01_variables_and_types.ipynb
│   ├── 02_input_output.py
│   ├── 03_operators.py
│   ├── exercises/
│   │   ├── exercise_01_profile.py
│   │   ├── exercise_02_calculator.py
│   │   └── challenge_employee_badge.py
│   └── solutions/
│       ├── exercise_01_profile_solution.py
│       ├── exercise_02_calculator_solution.py
│       └── challenge_employee_badge_solution.py
│
├── 02_control_flow/
│   ├── README.md
│   ├── 01_conditionals.ipynb
│   ├── 02_for_loops.ipynb
│   ├── 03_while_loops.py
│   ├── exercises/
│   └── solutions/
│
├── 03_data_structures/
│   ├── README.md
│   ├── 01_lists_tuples_sets.ipynb
│   ├── 02_dictionaries.ipynb
│   ├── 03_nested_data.py
│   ├── exercises/
│   ├── solutions/
│   └── mini_project/
│       └── contact_manager_cli.py
│
├── 04_functions_modules/
│   ├── README.md
│   ├── 01_functions.ipynb
│   ├── 02_scope_and_parameters.py
│   ├── 03_modules_packages.ipynb
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── formatters.py
│   ├── exercises/
│   └── solutions/
│
├── 05_files_errors_json/
│   ├── README.md
│   ├── 01_exceptions.ipynb
│   ├── 02_files.py
│   ├── 03_csv_json.ipynb
│   ├── data/
│   │   ├── users.csv
│   │   └── sample_users.json
│   ├── exercises/
│   └── solutions/
│
├── 06_oop/
│   ├── README.md
│   ├── 01_classes_objects.ipynb
│   ├── 02_encapsulation.py
│   ├── 03_inheritance_composition.ipynb
│   ├── models/
│   │   ├── user.py
│   │   ├── employee.py
│   │   └── notification.py
│   ├── exercises/
│   ├── solutions/
│   └── mini_project/
│       └── ticket_system.py
│
├── 07_web_api_intro/
│   ├── README.md
│   ├── 01_http_json_api.ipynb
│   ├── 02_fastapi_basics.py
│   ├── 03_pydantic_models.py
│   ├── exercises/
│   └── solutions/
│
├── 08_database/
│   ├── README.md
│   ├── 01_sqlite_intro.ipynb
│   ├── 02_crud_sqlite.py
│   ├── database.py
│   ├── exercises/
│   └── solutions/
│
├── final_project/
│   ├── README.md
│   ├── PROJECT_REQUIREMENTS.md
│   ├── ARCHITECTURE.md
│   ├── requirements.txt
│   ├── .env.example
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   │
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── user_repository.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── user_service.py
│   │   │   └── email_service.py
│   │   │
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── users.py
│   │   │   └── dashboard.py
│   │   │
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   ├── users.html
│   │   │   ├── user_form.html
│   │   │   └── user_detail.html
│   │   │
│   │   └── static/
│   │       ├── css/
│   │       │   └── styles.css
│   │       └── js/
│   │           └── app.js
│   │
│   ├── tests/
│   │   ├── test_users.py
│   │   └── test_email_service.py
│   │
│   └── data/
│       └── app.db
│
├── assessments/
│   ├── quiz_session_01.md
│   ├── quiz_session_02.md
│   ├── quiz_session_03.md
│   ├── quiz_session_04.md
│   ├── quiz_session_05.md
│   ├── quiz_session_06.md
│   └── final_project_rubric.md
│
└── resources/
    ├── python_cheatsheet.md
    ├── git_cheatsheet.md
    ├── debugging_guide.md
    └── common_errors.md
```

---

## 6. Course Sessions

### Session 1 — Python Fundamentals

Topics:

- What Python is
- Running `.py` files
- Jupyter notebooks
- `print()`
- comments
- variables
- naming conventions
- strings
- integers
- floats
- booleans
- `None`
- `type()`
- type conversion
- `input()`
- arithmetic operators
- comparison operators
- logical operators
- formatted strings / f-strings

Required practical exercises:

- Create a personal profile.
- Calculate age or years of service.
- Build a basic calculator.
- Generate an employee information card.

Cumulative project component:

Create a script that captures a user's:

- name
- email
- department
- age

and prints a formatted registration summary.

---

### Session 2 — Conditions and Loops

Topics:

- `if`
- `elif`
- `else`
- nested conditions
- boolean logic
- `for`
- `range()`
- `while`
- `break`
- `continue`

Exercises:

- age validation
- access level validation
- login attempt simulator
- employee classification
- processing a list of users

Cumulative project component:

Add validation to the user registration program.

Examples:

- reject empty names
- verify minimum age
- classify users by department
- repeat data capture until valid values are entered

---

### Session 3 — Data Structures

Topics:

- lists
- tuples
- sets
- dictionaries
- indexing
- slicing
- list methods
- dictionary methods
- nested structures
- looping through data structures
- basic comprehensions

Exercises:

- employee list
- inventory list
- unique departments
- user dictionary
- list of dictionaries
- search a user by ID

Mini-project:

Build a CLI Contact Manager capable of:

- adding contacts
- listing contacts
- searching contacts
- deleting contacts

Cumulative project component:

Replace individual user variables with dictionaries and collections.

---

### Session 4 — Functions, Modules, Errors, Files and JSON

Topics:

- defining functions
- parameters
- arguments
- return values
- default parameters
- keyword arguments
- scope
- imports
- modules
- packages
- reusable utility functions
- `try`
- `except`
- `else`
- `finally`
- reading files
- writing files
- CSV
- JSON

Exercises:

- email validation function
- reusable employee formatter
- save users to JSON
- load users from JSON
- handle invalid files
- import helper modules

Cumulative project component:

Refactor the registration application into modules and persist registered users in JSON.

---

### Session 5 — Object-Oriented Programming

Topics:

- procedural vs OOP
- classes
- objects
- `__init__`
- instance attributes
- instance methods
- class attributes
- `__str__`
- encapsulation
- inheritance
- composition
- basic polymorphism

Required classes:

```python
User
Employee
Notification
EmailNotification
Ticket
```

Exercises:

- convert user dictionary to a `User` class
- create `Employee(User)`
- notification classes
- ticket assignment system

Mini-project:

Build an object-oriented support ticket manager.

Cumulative project component:

Refactor users and notifications into classes.

---

### Session 6 — FastAPI, SQLite and Final Project

Topics:

- web application basics
- client/server concept
- HTTP
- GET
- POST
- PUT
- DELETE
- status codes
- JSON
- FastAPI
- routes
- request models
- Pydantic
- templates
- forms
- SQLite
- CRUD
- environment variables
- email sending
- application structure

Students must finish the integrated final project.

---

## 7. Final Project

# User Management & Notification Portal

Build a small administrative web application using Python and FastAPI.

The application should demonstrate the concepts taught throughout the course.

### Core Use Case

An administrator can register users through a web interface, store their information, view registered users, edit them, delete them, search them, and send a confirmation email.

### Required User Fields

Each user must contain at least:

```text
id
first_name
last_name
email
department
role
active
created_at
```

Optional fields:

```text
phone
employee_id
comments
```

---

## 8. Final Project Functional Requirements

The application must provide:

### Dashboard

Route:

```text
/
```

Display:

- total users
- active users
- inactive users
- total departments
- recently registered users

### User Registration

Routes:

```text
GET  /users/new
POST /users
```

The form must validate:

- required name
- valid email
- department
- role

When registration succeeds:

1. Store the user in SQLite.
2. Display a confirmation page or success message.
3. Attempt to send a welcome email.
4. Log the result of the email attempt.

### List Users

Route:

```text
GET /users
```

Display users in an HTML table.

Include:

- ID
- employee ID
- name
- email
- department
- role
- status
- actions

### User Details

Route:

```text
GET /users/{user_id}
```

### Edit User

Routes:

```text
GET  /users/{user_id}/edit
POST /users/{user_id}/edit
```

### Delete User

Route:

```text
POST /users/{user_id}/delete
```

### Search

Allow searching by:

- name
- email
- employee ID
- department

---

## 9. REST API Endpoints

In addition to HTML pages, expose a small JSON API.

Required endpoints:

```text
GET    /api/users
GET    /api/users/{id}
POST   /api/users
PUT    /api/users/{id}
DELETE /api/users/{id}
```

Use Pydantic schemas.

Return correct HTTP status codes.

---

## 10. Database Requirements

Use SQLite.

Prefer SQLAlchemy or SQLModel.

Create a reusable database layer.

Do not write SQL directly inside FastAPI route handlers.

Recommended layers:

```text
Router
  ↓
Service
  ↓
Repository
  ↓
Database
```

This structure should remain understandable for beginner/intermediate students.

---

## 11. Email Functionality

Create an `EmailService` class.

The service must support development mode.

Do not hardcode credentials.

Use environment variables such as:

```text
SMTP_HOST
SMTP_PORT
SMTP_USER
SMTP_PASSWORD
SMTP_FROM
SMTP_USE_TLS
```

Create `.env.example`.

If SMTP credentials are unavailable, the application must not crash.

Instead, provide a development fallback that writes email contents to:

```text
logs/emails/
```

Each simulated email can be saved as a `.txt` file.

This allows the instructor to demonstrate email workflows without requiring real corporate credentials.

---

## 12. Object-Oriented Programming Requirements in Final Project

OOP must not be included artificially.

Use classes where they have a clear purpose.

Examples:

```python
class EmailService:
    ...

class UserService:
    ...

class UserRepository:
    ...
```

Demonstrate:

- encapsulation
- dependency separation
- composition

For example:

```python
class UserService:
    def __init__(self, repository, email_service):
        self.repository = repository
        self.email_service = email_service
```

Explain this code in student-friendly terms.

---

## 13. Notebook Requirements

Each `.ipynb` notebook must include:

- lesson title
- learning objectives
- short explanations
- executable code cells
- examples
- guided exercises
- challenge exercises
- expected output where useful
- common mistakes
- summary
- connection to final project

Do not place full solutions immediately below exercises.

Solutions must be located separately.

Notebook code must execute from top to bottom without hidden dependencies.

---

## 14. Python File Requirements

Every `.py` file should:

- run independently where appropriate
- contain clear variable names
- follow PEP 8 reasonably
- avoid overengineering
- include concise comments only where educationally useful
- include `if __name__ == "__main__":` when appropriate

Student exercise files should contain:

```python
# TODO:
```

markers showing where students need to write code.

---

## 15. Exercise Difficulty

For every important topic, generate three levels:

### Guided

Students modify or complete partially written code.

### Independent

Students solve the problem from a written requirement.

### Challenge

Students combine several concepts without step-by-step instructions.

Do not make all exercises trivial.

---

## 16. Progressive Projects

Include these cumulative mini-projects:

### Project 1 — Employee Badge Generator

Concepts:

- variables
- strings
- input
- formatting

### Project 2 — Access Validation System

Concepts:

- conditions
- booleans

### Project 3 — Contact Manager CLI

Concepts:

- lists
- dictionaries
- loops

### Project 4 — User File Manager

Concepts:

- functions
- JSON
- files
- exceptions

### Project 5 — Support Ticket System

Concepts:

- classes
- inheritance
- composition

### Project 6 — User Management & Notification Portal

Concepts:

- FastAPI
- Pydantic
- HTML forms
- SQLite
- CRUD
- OOP
- email
- modular project architecture

Each project should reuse concepts from previous projects.

---

## 17. Assessments

Create a short assessment after each session.

Each quiz should contain approximately:

- 5 multiple-choice questions
- 2 code-reading questions
- 2 short coding questions
- 1 debugging question

Provide answers in an instructor-only section or separate solution file.

---

## 18. Final Project Rubric

Create a 100-point rubric.

Recommended weighting:

```text
Python fundamentals           10
Control flow                  10
Functions and modularity      10
Data structures               10
Object-oriented programming   15
Database / CRUD               15
FastAPI                       15
Validation / error handling    5
Email functionality            5
Code quality / documentation   5
```

Include evaluation criteria for:

- functionality
- readability
- modularity
- correct use of Python
- user experience
- error handling

---

## 19. Instructor Guide

`INSTRUCTOR_GUIDE.md` must include:

- session-by-session teaching plan
- expected timing
- live coding recommendations
- which files to open
- expected student difficulties
- common errors
- discussion questions
- suggested homework
- final project checkpoints

The instructor should be able to teach directly from this guide.

---

## 20. Student Guide

`STUDENT_GUIDE.md` must explain:

- how to install Python
- how to create a virtual environment
- how to activate it on Windows
- how to install dependencies
- how to run `.py` files
- how to launch Jupyter
- how to run FastAPI
- how to access Swagger docs
- how to reset the SQLite database
- how to use `.env`
- how to submit the final project

Prioritize Windows instructions while mentioning macOS/Linux equivalents when useful.

---

## 21. README Requirements

The root `README.md` should contain:

- course description
- prerequisites
- learning outcomes
- repository structure
- setup
- course sequence
- final project overview
- required software
- quick-start commands

Example commands:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter:

```bash
jupyter notebook
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

---

## 22. Dependencies

Prefer a small dependency set.

Example:

```text
fastapi
uvicorn[standard]
jinja2
python-multipart
sqlalchemy
pydantic
python-dotenv
email-validator
jupyter
pytest
httpx
```

Do not add libraries without a clear educational purpose.

---

## 23. Code Quality Rules

All generated code must:

- be runnable
- avoid syntax errors
- use consistent naming
- avoid placeholder imports
- avoid undefined variables
- avoid fake functions that are never implemented
- include dependency files
- use relative/project-safe paths where possible
- work on Windows

Before completing the repository, verify imports and run available tests.

---

## 24. Codex CLI Execution Strategy

Do not attempt to generate every file as one giant response.

Build the repository incrementally.

### Phase 1

Create:

- repository skeleton
- root documentation
- requirements
- setup module

### Phase 2

Create Sessions 1–3.

Validate all `.py` files.

### Phase 3

Create Sessions 4–6.

Validate imports and notebooks.

### Phase 4

Create final project.

Run the FastAPI application and automated tests.

### Phase 5

Create assessments, solutions, instructor resources, and final documentation.

### Phase 6

Perform repository-wide validation.

---

## 25. Validation Checklist

Before declaring the project finished, Codex must verify:

- [ ] Repository structure exists.
- [ ] All required `.py` files exist.
- [ ] All required `.ipynb` files exist.
- [ ] Python files compile.
- [ ] Imports resolve.
- [ ] `requirements.txt` exists.
- [ ] `.env.example` exists.
- [ ] FastAPI app starts.
- [ ] SQLite database initializes.
- [ ] User creation works.
- [ ] User listing works.
- [ ] User editing works.
- [ ] User deletion works.
- [ ] API endpoints work.
- [ ] Email fallback works without SMTP credentials.
- [ ] Tests execute.
- [ ] Exercise solutions are separated from student files.
- [ ] Instructor guide exists.
- [ ] Student guide exists.
- [ ] Final project rubric exists.
- [ ] README commands are correct.

If something fails, fix it before finishing.

---

## 26. Important Constraints

Do not:

- use Django for this version
- require paid APIs
- require cloud services
- require corporate email credentials
- use unnecessarily complex frontend frameworks
- introduce Docker before students understand the base project
- expose secrets
- hardcode passwords
- put all logic in `main.py`
- make all course examples unrelated to one another
- provide incomplete pseudo-code where runnable code is expected

Use:

- Python
- Jupyter
- FastAPI
- SQLite
- HTML
- CSS
- Jinja2
- Pydantic
- SQLAlchemy or SQLModel
- pytest

JavaScript should be optional and minimal.

---

## 27. Codex Final Instruction

Act as both:

1. a Python curriculum designer, and
2. a senior Python developer reviewing an educational repository.

Generate complete files rather than only describing what files should contain.

Prioritize clarity and teachability over clever code.

The code must gradually evolve from beginner scripts into a clean, modular FastAPI application so students can see how basic Python concepts translate into a real software project.

When creating each module, explicitly connect new concepts to previously learned material.

After completing each phase:

1. inspect the files created,
2. run or validate relevant Python code,
3. fix obvious errors,
4. continue to the next phase.

At the end, provide a concise completion report containing:

- files created
- tests executed
- commands used to run the course
- commands used to run the final project
- any optional improvements not required for the base course
