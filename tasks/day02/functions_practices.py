def eligible_to_vote(age, citizen):
    if age >= 18 and citizen == "USA":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")


eligible_to_vote(17, "USA")
eligible_to_vote(20, "USA")
eligible_to_vote(25, "CA")


def grade(grade):
    score = ""

    if grade != 'A' and grade != "B" and grade != "C" and grade != "D" and grade != "F":
        print("invalid score")
    else:
        if grade == "A":
            score = "excellent"
        if grade == "B":
            score = "great job"
        if grade == "C":
            score = "good"
        if grade == "D":
            score = "passed"
        if grade == "F":
            score = "failed"
        print(score)


grade("A")
grade("B")
grade("C")
grade("D")
grade("F")
grade("Z")


def number_type(num):
    if num > 0:
        print("positive")
    if num < 0:
        print("negative")
    if num == 0:
        print("zero")


number_type(15)
number_type(-2)
number_type(0)


def palindrome(word):
    rev = ""
    for i in reversed(range(0, len(word))):
        rev += (word[i])
    if word == rev:
        print("palindrome")
    else:
        print("not palindrome")


palindrome("madam")
palindrome("car")
