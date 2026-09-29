"""Build dependency-free trainer PDF guides for every course module.

The small PDF writer uses standard Helvetica and wrapped text so guides can be
regenerated on a clean classroom computer without additional libraries.
"""

from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "trainer_guides"

COMMON = """Delivery pattern
1. Explain the idea briefly and ask learners to predict a result.
2. Run the simple example, then connect it to an employee/user workflow.
3. Pair learners for the guided task; require an individual attempt next.
4. Use the challenge as the cumulative project increment.
5. Review the quiz and ask learners to explain, not only show, their code.

Trainer key points
- Keep live coding visible and deliberate. Normalize reading tracebacks.
- Ask what type and value each expression produces before running it.
- Let TODO files remain student-owned; open solutions only during review.
- Check boundary and failure cases, not only the happy path.
- End by tracing how the topic appears in the final portal.
"""

GUIDES = {
"00_setup": """Python and Jupyter Setup

Purpose and outcomes
Prepare a reproducible Windows-first environment. Learners verify Python 3.11+, create an isolated virtual environment, install dependencies, run a script, and execute a notebook from top to bottom.

Project and exercise walkthrough
- environment_check.py reports interpreter path/version and detects FastAPI, SQLAlchemy, Pydantic, Jinja2, and pytest. Ask learners why the executable path matters.
- 00_python_setup.ipynb introduces cell execution, variables, f-strings, and kernel state. Guided work customizes a greeting; the challenge reports Python and operating-system information.
- Validation: run the environment check and Restart Kernel / Run All. A pass means the expected interpreter and dependencies are visible.

Common difficulties and coaching
Windows may use the Microsoft Store alias or block activation scripts. Demonstrate `python -m pip` to bind pip to the correct interpreter. Explain that notebook cells share state and hidden order is dangerous.

Project connection
The same environment launches every script, notebook, test, and the final Uvicorn server.
""",
"01_fundamentals": """Session 1: Python Fundamentals

Purpose and outcomes
Learners create variables, inspect types, convert input, use arithmetic/comparison/logical operators, and produce formatted output with f-strings.

Examples and exercises
- 01_variables_and_types.ipynb models an employee with string, integer, float, Boolean, and None values. Guided work creates department and employee-count variables. The independent challenge calculates service years.
- 02_input_output.py captures name, email, department, and age, normalizes text, and returns a registration summary. Highlight that input always returns text.
- 03_operators.py calculates gross pay, eligibility, and a service milestone.
- exercise_01_profile.py is guided variable/f-string practice. Success: one sentence uses all fields with correct types.
- exercise_02_calculator.py independently captures two decimals and an operator. Discuss division by zero as a preview, not a requirement yet.
- challenge_employee_badge.py combines input, normalization, alignment, and formatting into Project 1.

Trainer key points specific to this module
Contrast expression, statement, variable, and value with concrete output. Show `type()` and conversions live. Watch for quoted numbers, invalid identifiers, and string concatenation type errors. Ask which portal fields are naturally Boolean or optional.

Assessment evidence
Learners can explain why `int(input())` is needed and produce a readable badge without copying the solution.
""",
"02_control_flow": """Session 2: Conditions and Loops

Purpose and outcomes
Translate business rules into if/elif/else branches and process repeated work with for, range, while, break, and continue.

Examples and exercises
- 01_conditionals.ipynb validates age/active state and guides department classification.
- 02_for_loops.ipynb numbers users and models bounded attempts. Guided work skips inactive records and stops at a target ID.
- 03_while_loops.py implements a three-attempt PIN workflow with clear remaining-attempt feedback.
- exercise_01_age_validation.py covers invalid, minor, and adult boundaries.
- exercise_02_process_users.py skips blank entries while preserving correct numbering.
- challenge_access_system.py is Project 2: validate role and active status repeatedly, allow quitting, and explain denial.

Trainer key points specific to this module
Have learners state rules in plain language before code. Draw branch paths and dry-run one loop iteration at a time. Test ages -1, 17, and 18. Watch indentation, `=` versus `==`, conditions that can never run, and infinite while loops.

Portal connection and evidence
Validation controls registration; loops process database results. Learners should demonstrate accepted, rejected, invalid, and quit paths.
""",
"03_data_structures": """Session 3: Data Structures

Purpose and outcomes
Choose lists, tuples, sets, or dictionaries based on ordering, mutability, uniqueness, and key-based access; work with nested records and comprehensions.

Examples and exercises
- 01_lists_tuples_sets.ipynb practices indexing, slicing, append, immutable coordinates, and unique departments.
- 02_dictionaries.ipynb creates and updates a user, loops through items, safely reads optional keys, and filters nested data.
- 03_nested_data.py searches users by ID and derives active names/departments.
- exercise_01_collections.py is guided modification, slicing, deduplication, and tuple work.
- exercise_02_user_search.py independently finds a matching dictionary or reports absence.
- challenge_inventory.py combines CRUD-like inventory operations and a low-stock comprehension.
- contact_manager_cli.py is Project 3: add, list, search, and delete contact dictionaries through a menu loop.

Trainer key points specific to this module
Ask learners to justify the data structure before coding. Contrast an index with a dictionary key. Demonstrate `.get()` for optional values and warn against mutating a list during iteration. Trace one contact from input to nested dictionary to displayed result.

Assessment evidence
The contact manager handles empty collections, case-insensitive search, missing deletes, and repeated actions.
""",
"04_functions_modules": """Session 4A: Functions and Modules

Purpose and outcomes
Extract repeated logic into small functions, distinguish printing from returning, use default/keyword arguments and scope, and organize reusable packages.

Examples and exercises
- 01_functions.ipynb builds a `full_name` function and guides a configurable department label. Its challenge separates capture, validation, and formatting.
- 02_scope_and_parameters.py builds email addresses with module-level defaults and local variables.
- 03_modules_packages.ipynb introduces standard/local imports and `__init__.py` interfaces.
- utils/validators.py and formatters.py provide reusable email/non-empty validation and employee formatting.
- exercise_01_email_function.py is guided validation. exercise_02_formatter.py independently returns a formatted line. challenge_registration_package.py imports both helpers into a registration workflow.

Trainer key points specific to this module
Ask “What goes in, what comes out, and what side effect occurs?” Require functions that return reusable values. Demonstrate working-directory import problems without hiding them. Avoid premature abstraction: one purpose per helper is enough.

Portal connection and evidence
The portal divides routes, services, and repositories into modules. Learners can import helpers and test them with several arguments.
""",
"05_files_errors_json": """Session 4B: Errors, Files, CSV, and JSON

Purpose and outcomes
Handle predictable failures with specific exceptions and persist structured user records with safe pathlib paths, CSV, and JSON.

Examples and exercises
- 01_exceptions.ipynb demonstrates try/except/else/finally and guides safe division.
- 02_files.py writes and reads a text report relative to its module, avoiding fragile current-directory assumptions.
- 03_csv_json.ipynb converts CSV rows to JSON-shaped dictionaries and distinguishes serialized text from Python objects.
- users.csv and sample_users.json provide realistic input data.
- exercise_01_safe_number.py is guided ValueError handling. exercise_02_json_users.py independently writes/loads JSON and handles missing or corrupt files.
- challenge_user_file_manager.py is Project 4: functions for load, save, add, list, search, and delete with persistence.

Trainer key points specific to this module
Catch only errors the code can explain or recover from. Keep try blocks narrow. Corrupt a copy of JSON live and inspect the traceback before handling it. Discuss encoding and why secrets do not belong in data files.

Portal connection and evidence
JSON becomes API payloads; SQLite later replaces the file while preserving CRUD concepts. Verify persistence across two program runs.
""",
"06_oop": """Session 5: Object-Oriented Programming

Purpose and outcomes
Model cohesive data and behavior with classes/objects, __init__, methods, class attributes, __str__, encapsulation, inheritance, composition, and simple polymorphism.

Examples and exercises
- 01_classes_objects.ipynb creates User instances and guides active-state behavior.
- models/user.py encapsulates normalized user state; Employee(User) adds employee ID/department; Notification and EmailNotification share a send interface.
- 02_encapsulation.py changes ticket status only through a validated method.
- 03_inheritance_composition.ipynb composes TicketService with a replaceable notifier.
- exercise_01_user_class.py is guided. exercise_02_employee.py independently applies inheritance/super. challenge_notifications_tickets.py combines required classes.
- ticket_system.py is Project 5: Ticket, Agent, polymorphic Notification, and a composed TicketManager.

Trainer key points specific to this module
Use “is-a” for inheritance and “uses-a/has-a” for composition. Show why `_status` signals controlled access. Watch forgotten `self`, mutable class state, missing `super()`, and inheritance used only to reuse code.

Portal connection and evidence
UserService composes repository and email service. Learners can swap a notifier without editing ticket logic.
""",
"07_web_api_intro": """Session 6A: HTTP, FastAPI, and Pydantic

Purpose and outcomes
Explain client/server exchange, routes, HTTP methods/status codes, JSON, request schemas, and automatic API documentation.

Examples and exercises
- 01_http_json_api.ipynb maps actions to GET/POST/PUT/DELETE and status codes 200, 201, 204, 404.
- 02_fastapi_basics.py exposes root/list/create/detail routes over an in-memory list and returns 404 for missing users.
- 03_pydantic_models.py validates required text, EmailStr, and an age range.
- exercise_01_routes.py is guided health/departments routing. exercise_02_schema.py independently constrains a ticket. challenge_user_api.py completes in-memory CRUD.

Trainer key points specific to this module
Use Swagger `/docs` as an interactive client and inspect request/response bodies. Distinguish route parameters, query parameters, forms, and JSON. Explain 422 as useful validation feedback and 404 as a resource result, not a server crash.

Portal connection and evidence
Learners can create valid JSON, interpret rejected input, and select correct methods/statuses before adding persistence.
""",
"08_database": """Session 6B: SQLite and CRUD

Purpose and outcomes
Persist records in SQLite, create tables, use parameterized statements, commit/rollback safely, and isolate data access in a repository.

Examples and exercises
- 01_sqlite_intro.ipynb uses an in-memory database for independent, repeatable CREATE/INSERT/SELECT practice.
- database.py provides a project-safe connection context manager, row mapping, commit, rollback, close, and initialization.
- 02_crud_sqlite.py implements create, list, update, and delete functions outside any route.
- exercise_01_create_read.py is guided initialization/insertion/listing. exercise_02_update_delete.py handles missing IDs. challenge_repository.py moves CRUD into a class without UI calls.

Trainer key points specific to this module
Draw table, row, column, primary key, and unique constraint. Always demonstrate placeholders rather than string-formatted SQL. Explain transaction boundaries and why `commit` matters. Delete only a disposable lesson database when demonstrating reset.

Portal connection and evidence
The final SQLAlchemy repository preserves these responsibilities. Learners demonstrate CRUD and verify changes survive reconnecting.
""",
"final_project": """Session 6C: User Management and Notification Portal

Purpose and outcomes
Integrate Python fundamentals, validation, collections, functions, OOP, HTTP, templates, SQLite, CRUD, email, environment variables, and tests in an administrative application.

Architecture walkthrough
Browser/API client -> FastAPI router -> UserService -> UserRepository -> SQLAlchemy/SQLite. UserService also composes EmailService, which uses SMTP when completely configured and writes a timestamped text message otherwise. Schemas validate boundary input; the SQLAlchemy model represents persisted state.

Required project workflows
- Dashboard: total, active, inactive, department count, and five recent users.
- HTML: register, confirmation, searchable table, details, edit, delete with confirmation.
- JSON API: list/detail/create/update/delete with 200/201/204/404/409/422 behavior.
- User fields: names, email, department, role, active, creation timestamp, plus optional phone, employee ID, comments.
- Operations: initialize data/app.db, keep credentials in .env, log simulated email under logs/emails, run pytest.

Exercise/checkpoint sequence
1. Launch `/health` and `/docs`; identify every layer for GET `/api/users`.
2. Create a user in Swagger, then find it in the HTML list and database-backed dashboard.
3. Search by each supported field; edit status/department; inspect detail output.
4. Delete the record and verify both UI and API return the expected result.
5. Run without SMTP, inspect the email text file, and explain the fallback.
6. Run tests/test_users.py and tests/test_email_service.py; trace one failure if introduced.

Trainer key points specific to this module
Run Uvicorn from `final_project`, never expose `.env`, and keep SQL outside handlers. Trace one request end to end before learners change code. Distinguish model (database), schema (boundary contract), repository (persistence), service (workflow), and router (HTTP). Assess functionality first, then readability and presentation.

Completion evidence
All HTML/API CRUD paths work, invalid/duplicate input is handled, SQLite initializes, fallback email is readable, tests pass, and the learner can explain composition in UserService.
""",
}


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def layout_lines(title: str, content: str) -> list[list[tuple[str, int, bool]]]:
    pages: list[list[tuple[str, int, bool]]] = [[]]
    pages[0].append((title, 20, True))
    pages[0].append(("Trainer Reference Guide", 11, False))
    for raw in (content.strip() + "\n\n" + COMMON.strip()).splitlines():
        raw = raw.strip()
        if not raw:
            pages[-1].append(("", 6, False))
            continue
        heading = not raw.startswith(("-", "1.", "2.", "3.", "4.", "5.")) and len(raw) < 45
        width = 72 if heading else 88
        prefix = "" if not raw.startswith("-") else "- "
        body = raw[2:] if raw.startswith("-") else raw
        wrapped = textwrap.wrap(body, width=width, subsequent_indent="  ") or [""]
        for index, line in enumerate(wrapped):
            value = (prefix if index == 0 else "  ") + line
            pages[-1].append((value, 13 if heading else 10, heading))
            if len(pages[-1]) >= 45:
                pages.append([])
    return [page for page in pages if page]


def build_pdf(module: str, content: str) -> Path:
    title = content.splitlines()[0]
    pages = layout_lines(title, "\n".join(content.splitlines()[1:]))
    objects: list[bytes] = []
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    kids = " ".join(f"{4 + index * 2} 0 R" for index in range(len(pages)))
    objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>".encode())
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    for page_number, page in enumerate(pages, 1):
        page_id = 4 + (page_number - 1) * 2
        stream_id = page_id + 1
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            f"/Resources << /Font << /F1 3 0 R >> >> /Contents {stream_id} 0 R >>".encode())
        commands = ["BT", "/F1 10 Tf", "0.12 0.18 0.30 rg", "54 744 Td"]
        previous_size = 10
        for line, size, bold in page:
            leading = 22 if size >= 20 else (18 if size >= 13 else 13)
            commands.extend([f"0 -{leading} Td", f"/F1 {size} Tf"])
            if size >= 13:
                commands.append("0.10 0.28 0.52 rg")
            else:
                commands.append("0.12 0.14 0.18 rg")
            commands.append(f"({pdf_escape(line)}) Tj")
            previous_size = size
        commands.extend(["0 -18 Td", "/F1 8 Tf", "0.4 0.4 0.4 rg",
                         f"(Python Course 2026  |  {module}  |  Page {page_number} of {len(pages)}) Tj", "ET"])
        stream = "\n".join(commands).encode("latin-1", errors="replace")
        objects.append(f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"\nendstream")
    output = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, obj in enumerate(objects, 1):
        offsets.append(len(output))
        output.extend(f"{number} 0 obj\n".encode() + obj + b"\nendobj\n")
    xref = len(output)
    output.extend(f"xref\n0 {len(objects)+1}\n0000000000 65535 f \n".encode())
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode())
    output.extend(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    path = OUTPUT / f"{module}_trainer_guide.pdf"
    path.write_bytes(output)
    return path


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    for module, content in GUIDES.items():
        path = build_pdf(module, content)
        print(f"built {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
