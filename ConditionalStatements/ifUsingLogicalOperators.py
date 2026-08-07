#Using Logical Operators
age = 20
citizen = True

if age <= 15 and citizen:
    print("15 not Eligible to vote ")
elif age >= 18 and citizen:
    print("18 Eligible to vote")

else:
    print("no Eligible")

    