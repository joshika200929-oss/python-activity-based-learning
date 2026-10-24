
n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = int(input("Enter subject marks: "))

    # Apply grace marks if needed
    if m < 35 and m >= 32:
        m = m + 3

    if m > 100:
        m = 100

    marks.append(m)

print("\nFinal Marks:")

total = 0
for i in range(n):
    print("Subject", i + 1, ":", marks[i])
    total = total + marks[i]

    if marks[i] < 35:
        print("Result: Fail")

if all(m >= 35 for m in marks):
    print("Result: Pass")
    percentage = total / n
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Classification: Distinction")
    elif percentage >= 60:
        print("Classification: First Class")
    elif percentage >= 50:
        print("Classification: Second Class")
    else:
        print("Classification: Pass Class")
else:
    print("Final Result: Fail")

print("Total Marks:", total, "/", n * 100)
