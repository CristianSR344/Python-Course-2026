# Debugging Guide

1. Read the final traceback line: exception type and message.
2. Open the first line in your own code mentioned by the traceback.
3. State the expected and actual values/types.
4. Reduce to the smallest reproducible input.
5. Add temporary `print(repr(value), type(value))` or use a debugger breakpoint.
6. Fix the cause, remove temporary output, and rerun the failing plus nearby cases.

For FastAPI, check the terminal log and `/docs`; distinguish 4xx client/validation responses from 5xx defects. For SQLite, confirm the actual database path and transaction commit. For imports, confirm the activated interpreter and current directory.

