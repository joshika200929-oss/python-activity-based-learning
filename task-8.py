
n = int(input("Enter number of subjects: "))

total1 = 0
total2 = 0
weak = 0

for i in range(n):
    subject = input("\nEnter subject name: ")
    m1 = int(input("Enter first exam marks: "))
    m2 = int(input("Enter second exam marks: "))

    total1 = total1 + m1
    total2 = total2 + m2

    if m2 > m1:
        print(subject, ": Improved by", m2 - m1)
    elif m2 < m1:
        print(subject, ": Declined by", m1 - m2)
    else:
        print(subject, ": No change")

    if m2 < 40:
        print(subject, "is a weak subject")
        weak = weak + 1

avg = total2 / n

print("\nFirst Exam Total:", total1)
print("Second Exam Total:", total2)

if total2 > total1:
    print("Overall Performance: Improved")
elif total2 < total1:
    print("Overall Performance: Declined")
else:
    print("Overall Performance: No Change")

print("Weak Subjects:", weak)

if avg >= 75:
    print("Classification: Excellent")
elif avg >= 60:
    print("Classification: Good")
elif avg >= 40:
    print("Classification: Average")
else:
    print("Classification: Poor")
