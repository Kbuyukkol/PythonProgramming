positive = 0
negative = 0

for x in range(1, 6):
    num = int(input("Enter a number\n"))
    if num > 0:
        positive += 1
    if num < 0:
        negative += 1
print(f"{positive} positive and {negative} negative")
