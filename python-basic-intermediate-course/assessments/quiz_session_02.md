# Session 2 Quiz — Control Flow

## Multiple choice

1. Which checks equality? A) = B) == C) != D) :=
2. Which branch handles all unmatched cases? A) if B) for C) else D) break
3. What does `continue` do? A) exits program B) skips to next iteration C) repeats forever D) returns
4. What values come from `range(1, 4)`? A) 1,2,3 B) 1,2,3,4 C) 0,1,2,3 D) 4
5. Which loop is useful when repetitions are unknown? A) import B) if C) while D) class

## Read code

6. What prints? `for n in range(3): print(n)`
7. How many times runs? `attempts=2; while attempts>0: attempts -= 1`

## Write code

8. Print “adult” only when age is at least 18.
9. Loop through names and skip empty strings.

## Debug

10. Fix the infinite loop: `count=3; while count>0: print(count)`.

<details><summary>Instructor answers</summary>

1 B; 2 C; 3 B; 4 A; 5 C. 6: 0, 1, 2 on separate lines. 7: twice. 8: `if age >= 18: print("adult")`. 9: use `for`, `if not name: continue`. 10: add `count -= 1` inside the loop.
</details>

