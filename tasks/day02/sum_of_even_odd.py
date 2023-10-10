sum_of_evens = 0

for x in range(1, 101):
    if x % 2 == 0:
        sum_of_evens += x
print(sum_of_evens)

sum_of_odds = 0

for x in range(1, 101):
    if x % 2 != 0:
        sum_of_odds += x
print(sum_of_odds)

sum_of_any = 0

num = int(input("give me a positive number\n"))
for x in range(1, num+1):
    sum_of_any += x
print(sum_of_any)
