products = [{"sku": "A1", "name": "Keyboard", "quantity": 3}]
products.append({"sku": "B2", "name": "Mouse", "quantity": 8})
target = next((item for item in products if item["sku"] == "A1"), None)
if target:
    target["quantity"] += 2
products[:] = [item for item in products if item["sku"] != "B2"]
print([item for item in products if item["quantity"] < 6])

