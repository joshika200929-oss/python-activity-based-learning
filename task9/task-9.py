
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print("\nEnter student details")
    name = input("Enter name: ")
    course = input("Enter course (CSE or ECE): ")

    maths = int(input("Enter Maths marks: "))
    subject = int(input("Enter other subject marks: "))
    aggregate = int(input("Enter aggregate percentage: "))

    if course == "CSE":
        cutoff = 80
    elif course == "ECE":
        cutoff = 70
    else:
        print("Invalid course")
        continue

    if maths >= 60 and subject >= 50 and aggregate >= cutoff:
        students.append([name, course, aggregate])
    else:
        print(name, "Not Eligible")

students.sort(key=lambda x: -x[2])

print("\n--- Admission Rank List ---")

for i in range(len(students)):
    print("Rank:", i + 1)
    print("Name:", students[i][0])
    print("Course:", students[i][1])
    print("Aggregate:", students[i][2])
