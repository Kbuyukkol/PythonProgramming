grade_level = int(input("What is your grade level number\n"))
grade_type = ""

if 1 <= grade_level <= 18:
    if 1 <= grade_level <= 5:
        grade_type = " Elementary school "
    if 6 <= grade_level <= 8:
        grade_type = " Middle school "
    if 9 <= grade_level <= 12:
        grade_type = " High school "
    if 13 <= grade_level <= 16:
        grade_type = " College "
    if 17 <= grade_level <= 18:
        grade_type = " Grad School "
    print(grade_type)
else:
    print("Invalid grade level")
