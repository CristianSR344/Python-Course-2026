first = float(input("First number: "))
operator = input("Operator (+, -, *, /): ").strip()
second = float(input("Second number: "))
operations = {"+": first + second, "-": first - second,
              "*": first * second, "/": first / second}
print(f"Result: {operations[operator]:g}")

