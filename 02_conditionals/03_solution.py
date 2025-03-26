score = 185

if score >= 101:
    print("Please verify your grade again")
    exit()
    # break    #  "break" can be used only within a loop

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)