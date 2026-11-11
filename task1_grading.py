NUM_STUDENTS = 10
PASS_MARK = 50

marks_list = []
grades_list = []
passed = 0
failed = 0

for i in range(1, NUM_STUDENTS + 1):
    while True:
        try:
            mark = float(input(f"Enter marks for student {i}: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if 0 <= mark <= 100:
            break
        else:
            print("Marks must be between 0 and 100. Try again.")

    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"

    if mark >= PASS_MARK:
        passed += 1
    else:
        failed += 1

    marks_list.append(mark)
    grades_list.append(grade)

print("\n----- Student Results -----")
for i in range(NUM_STUDENTS):
    print(f"Student {i + 1}: Marks = {marks_list[i]}, Grade = {grades_list[i]}")

highest = max(marks_list)
average = sum(marks_list) / NUM_STUDENTS

print("\n----- Class Summary -----")
print(f"Students Passed : {passed}")
print(f"Students Failed : {failed}")
print(f"Highest Mark    : {highest}")
print(f"Class Average   : {average:.2f}")
