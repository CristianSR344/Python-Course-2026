try:
    count = int(input("Employee count: "))
except ValueError:
    print("Enter a whole number.")
else:
    print(f"Count accepted: {count}")
finally:
    print("Validation finished")

