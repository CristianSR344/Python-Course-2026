# Common Errors

- `SyntaxError`: Python cannot parse the file; inspect punctuation near the caret.
- `IndentationError`: blocks do not use consistent indentation.
- `NameError`: a name is misspelled, out of scope, or used before assignment.
- `TypeError`: an operation received an incompatible type; remember input is text.
- `ValueError`: the type is appropriate but the value cannot be converted/accepted.
- `KeyError` / `IndexError`: dictionary key or sequence position is missing; validate first.
- `FileNotFoundError`: inspect the resolved path and prefer `Path(__file__)`-relative data.
- `ModuleNotFoundError`: activate the intended environment, install requirements, and run from the documented directory.
- `IntegrityError`: a database constraint (often unique email/employee ID) was violated; rollback and report a conflict.
- HTTP 422: submitted input did not match the Pydantic/form contract.

Do not hide errors with bare `except:`. Handle an error only when the program can recover or provide clearer context.

