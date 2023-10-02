name = input("Enter your full name\n")
hourly_rate = int(input("Enter your hourly rate\n"))
weekly_hours = int(input("How many hours you work in a week?\n"))

salary = float(hourly_rate * weekly_hours * 52)

print(f"Hello {name}, your salary is $ {salary}")
