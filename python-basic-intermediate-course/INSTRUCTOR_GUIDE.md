# Instructor Guide

## Delivery principles

Live-code small examples, narrate errors, and ask students to predict output before execution. Keep solutions closed during exercises. Every session ends with a working project increment and its quiz.

## Session plan

### Session 1 — Fundamentals (120 minutes)

- 0–30: open `01_variables_and_types.ipynb`; demonstrate values and conversions.
- 30–65: run the profile and calculator exercises.
- 65–105: build the employee badge and registration summary.
- 105–120: quiz and recap.

Watch for quoted numbers, invalid variable names, and forgetting that `input()` returns text. Ask: “Which user values need conversion?” Homework: customize the badge.

### Session 2 — Control flow (120 minutes)

- 0–35: conditionals and Boolean expressions.
- 35–70: loop exercises and login simulation.
- 70–105: access-validation project.
- 105–120: quiz.

Watch indentation, infinite loops, and boundary conditions. Ask students to state validation rules in plain language first. Checkpoint: registration rejects blank names and underage users.

### Session 3 — Data structures (120 minutes)

- 0–35: lists, sets, tuples, dictionaries.
- 35–65: search and nested-data exercises.
- 65–110: contact manager CLI.
- 110–120: quiz.

Common issues are confusing indexes with keys and mutating a list while iterating. Homework: add contact updating. Checkpoint: users are dictionaries stored in a list.

### Session 4 — Functions, modules, files (120 minutes)

- 0–30: functions, parameters, scope, and imports.
- 30–60: exceptions and validation utilities.
- 60–105: JSON user file manager.
- 105–120: quiz.

Open the `utils` package and contrast returning with printing. Demonstrate a missing/corrupt file. Checkpoint: registration is modular and persists users.

### Session 5 — OOP (120 minutes)

- 0–35: `User`, `Employee`, and encapsulation.
- 35–65: inheritance, polymorphism, and composition.
- 65–110: ticket manager.
- 110–120: quiz.

Students may overuse inheritance or forget `self`. Ask: “Does this object own, use, or specialize another object?” Checkpoint: user and notification behavior is represented by collaborating classes.

### Session 6 — Web, database, final project (120 minutes)

- 0–25: HTTP, routes, schemas, Swagger.
- 25–50: SQLite repository demonstration.
- 50–105: complete and test portal workflows.
- 105–120: final quiz and rubric review.

Open `final_project/app/main.py`, then trace router → service → repository. Demonstrate both the UI and `/docs`. Common issues include running Uvicorn from the wrong directory and form/API type differences. Final checkpoint: CRUD works, fallback email is logged, and tests pass.

## Assessment and differentiation

Use code-reading questions for discussion and coding questions for evidence. Advanced students can add pagination or database migrations; beginners should prioritize the required CRUD path. Grade with the 100-point rubric and verify behavior rather than visual polish alone.

