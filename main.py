name = input("Enter student name: ")
tamil = int(input("Enter Tamil mark: "))
english = int(input("Enter English mark: "))
python = int(input("Enter Python mark: "))
maths = int(input("Enter Maths mark: "))
total = tamil + english + python + maths
average = total / 4
print("\n----- STUDENT MARK DETAILS -----")
print("Name:", name)
print("Total:", total)
print("Average:", average)
if tamil < 35 or english < 35 or python < 35 or maths < 35:
    print("Result: FAIL")
elif average >= 90:
    print("Grade: A+")
    print("Result: PASS")
elif average >= 80:
    print("Grade: A")
    print("Result: PASS")
elif average >= 70:
    print("Grade: B")
    print("Result: PASS")
elif average >= 60:
    print("Grade: C")
    print("Result: PASS")
else:
    print("Grade: D")
    print("Result: PASS")
