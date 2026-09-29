users = [{"id": 10, "name": "Noor"}, {"id": 11, "name": "Sam"}]
target_id = 11
found = next((user for user in users if user["id"] == target_id), None)
print(found if found else "Not found")

