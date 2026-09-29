while True:
    role = input("Role (admin/manager/employee or quit): ").strip().lower()
    if role == "quit":
        break
    if role not in {"admin", "manager", "employee"}:
        print("Unknown role")
        continue
    active = input("Active (yes/no): ").strip().lower() == "yes"
    if active and role in {"admin", "manager"}:
        print("Administrative access granted")
    elif not active:
        print("Inactive accounts cannot sign in")
    else:
        print("Standard access only")

