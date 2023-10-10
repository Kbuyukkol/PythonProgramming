word = "A1B2C3"
number_of_digits = 0

for x in range(0, len(word)):
    number_of_digits += word.count(word[x])
print(number_of_digits)
