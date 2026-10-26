n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter aggregate marks: "))
    subject = int(input("Enter minimum subject marks: "))
    attendance = int(input("Enter attendance: "))
    income = int(input("Enter family income: "))

    if marks >= 75 and subject >= 60 and attendance >= 75 and income <= 250000:
        print(name, "Eligible for Scholarship")
    else:
        print(name, "Not Eligible for Scholarship")
