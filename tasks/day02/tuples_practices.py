words = ('Java', 'Anna', 'python', 'Level')

for x in words:
    if x[::-1].lower() == x.lower():
        print(x)

tuple1 = (1, 2, 3, 4, 5, 8)
tuple2 = (4, 5, 6, 7, 8)

for i in range(0, len(tuple1)):
    for j in range(0, len(tuple2)):
        if tuple1[i] == tuple2[j]:
            print(tuple1[i])

numbers = (1, 2, 3, 4, 5, 6, 7, 8)
count_of_evens = 0
count_of_odds = 0

for i in numbers:
    if i % 2 == 0:
        count_of_evens += 1
    if i % 2 != 0:
        count_of_odds += 1

print(f"There are {count_of_evens} even numbers and {count_of_odds} odd numbers")
