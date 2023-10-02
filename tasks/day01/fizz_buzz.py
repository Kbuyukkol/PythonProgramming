num = int(input("Give me a number\n"))
resource = ""

if num % 3 == 0 and num % 5 == 0:
    resource += "FizzBuzz"
elif num % 3 == 0:
    resource += "Fizz"
elif num % 5 == 0:
    resource += "Buzz"
print(resource)
