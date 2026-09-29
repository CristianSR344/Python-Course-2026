"""Arithmetic, comparison, and logical operator examples."""


def service_summary(start_year: int, current_year: int = 2026) -> str:
    years = current_year - start_year
    milestone = years >= 5
    return f"Service: {years} years | Five-year milestone: {milestone}"


if __name__ == "__main__":
    hourly_rate = 22.50
    hours = 40
    gross_pay = hourly_rate * hours
    eligible = hours >= 20 and gross_pay > 0
    print(f"Gross pay: ${gross_pay:.2f}; benefits eligible: {eligible}")
    print(service_summary(2020))

