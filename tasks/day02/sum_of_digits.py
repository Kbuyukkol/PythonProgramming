word = "mn@#123Ab!4"
sum_of_digits = 0


for x in range(0, len(word)):
    if word[x].isdigit():
        sum_of_digits += int(word[x])

print(sum_of_digits)
