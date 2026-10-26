
n = int(input("Enter number of months: "))
bills = []

for i in range(n):
    print("\nMonth", i + 1)
    units = int(input("Enter electricity units: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = bill + 50       # Fixed charge
    bill = bill + bill * 0.05  # 5% surcharge

    if units < 50:
        bill = bill - 20   # Rebate

    bills.append(bill)
    print("Electricity Bill: Rs.", round(bill, 2))

print("\nMonthly Bill Comparison")

for i in range(n):
    print("Month", i + 1, ":", round(bills[i], 2))

    if i > 0 and bills[i] > bills[i - 1] * 1.2:
        print("Unusual increase detected!")
