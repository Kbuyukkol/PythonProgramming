word = "mn@#123Ab!"
letters = ""
digits = ""
special = ""

for x in range(0, len(word)):
    if word[x].isalpha():
        letters += word[x]
    elif word[x].isdigit():
        digits += word[x]
    else:
        special += word[x]
print(letters)
print(digits)
print(special)
