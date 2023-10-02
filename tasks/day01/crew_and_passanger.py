number_of_people = int(input("How many people are there on the ship\n"))
crew = 0
passenger = 0

if number_of_people != 50 and number_of_people != 75 and number_of_people != 100:
    print("Invalid")
else:

    if number_of_people == 50:
        crew = 20
        passenger = (number_of_people - crew)
    if number_of_people == 75:
        crew = 25
        passenger = (number_of_people - crew)
    if number_of_people == 100:
        crew = 30
        passenger = (number_of_people - crew)
    print(f"{crew} crew, {passenger} passengers")
