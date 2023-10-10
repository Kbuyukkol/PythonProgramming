num = int(input("give me a positive number\n"))
factorial = 1

for x in range(1, num + 1):
    factorial *= x
print(factorial)
