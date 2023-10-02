grade = "A"
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

