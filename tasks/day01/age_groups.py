age = int(input("What is your age:\n"))
age_group = ""

if age < 0 or age > 150:
    print("invalid age")
else:
    if age < 21:
        age_group = "teenager"
    elif age <= 55:
        age_group = "adult"
    else:
        age_group = "senior"
    print(age_group)
