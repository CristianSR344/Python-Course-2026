# Session 3 Quiz — Data Structures

## Multiple choice

1. Which collection stores unique values? A) list B) tuple C) set D) string
2. Which is immutable? A) list B) tuple C) dict D) set
3. How is a dictionary value accessed? A) position only B) key C) type D) loop only
4. What does `items()` provide? A) indexes B) key/value pairs C) unique values D) lengths
5. Which selects first three list items? A) `[1:3]` B) `[:3]` C) `[3]` D) `[0:2]`

## Read code

6. What is `{x for x in ["IT", "HR", "IT"]}`?
7. What prints? `user={"name":"Ada"}; print(user.get("phone", "None"))`

## Write code

8. Append a user dictionary to a list.
9. Find a user with ID 7 in a list of dictionaries.

## Debug

10. Fix: `user = {"name": "Ada"}; print(user[0])`.

<details><summary>Instructor answers</summary>

1 C; 2 B; 3 B; 4 B; 5 B. 6: a set containing IT and HR. 7: `None`. 8: `users.append({"id": 1, "name": "Ada"})`. 9: loop/`next` comparing `user["id"]`. 10: `user["name"]`.
</details>

