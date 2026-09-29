# Session 4 Quiz — Functions, Modules, Files

## Multiple choice

1. What sends a value back from a function? A) print B) return C) import D) finally
2. A variable created inside a function is usually: A) global B) local C) JSON D) immutable
3. Which module handles JSON? A) csv B) pathlib C) json D) smtp
4. Which exception follows `int("x")`? A) KeyError B) ValueError C) IndexError D) TypeError
5. Which block always runs? A) else B) finally C) except only D) import

## Read code

6. What returns? `def label(name="User"): return name.upper(); label()`
7. Explain the difference between `json.dumps(data)` and `json.loads(text)`.

## Write code

8. Define an email-validation function with a Boolean return.
9. Safely load a file and handle `FileNotFoundError`.

## Debug

10. Fix a function that only prints when the caller needs its value.

<details><summary>Instructor answers</summary>

1 B; 2 B; 3 C; 4 B; 5 B. 6: `USER`. 7: dumps serializes to text; loads parses text. 8: accept a string and return an expression checking `@`/domain. 9: narrow `try` with specific `except`. 10: replace `print(result)` inside the function with `return result`.
</details>

