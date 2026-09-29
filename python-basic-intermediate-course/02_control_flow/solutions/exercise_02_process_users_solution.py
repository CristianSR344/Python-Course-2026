users = ["Ana", "", "Luis", "Mina"]
number = 0
for user in users:
    if not user:
        continue
    number += 1
    print(number, user)

