def format_employee(employee: dict[str, object]) -> str:
    """Return one consistently formatted employee line."""
    status = "active" if employee.get("active", False) else "inactive"
    return f"{employee.get('id', 'N/A')} | {employee['name']} | {status}"

