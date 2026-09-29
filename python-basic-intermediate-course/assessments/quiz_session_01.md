# Session 1 Quiz — Fundamentals

## Multiple choice

1. What type does `input()` return? A) int B) str C) bool D) None
2. Which name follows Python conventions? A) employee-name B) 2employees C) employee_name D) Employee Name
3. What is `type(3.5)`? A) float B) int C) str D) decimal
4. Which creates formatted text? A) `f"Age: {age}"` B) `"Age: age"` C) `format age` D) `print[age]`
5. What is `10 // 3`? A) 3.33 B) 3 C) 1 D) 4

## Read code

6. What prints? `years = "5"; print(int(years) + 1)`
7. Explain the value of `eligible = age >= 18 and active` for `age=18`, `active=False`.

## Write code

8. Capture a department and print it title-cased.
9. Calculate and display years of service from a start year.

## Debug

10. Fix: `age = input("Age: "); print(age + 1)`.

<details><summary>Instructor answers</summary>

1 B; 2 C; 3 A; 4 A; 5 B. 6: `6`. 7: `False`, because both sides of `and` must be true. 8: `department = input("Department: ").strip(); print(department.title())`. 9: convert input to int and subtract it from the current year. 10: `age = int(input("Age: "))`.
</details>

