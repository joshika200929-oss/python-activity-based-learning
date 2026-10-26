
balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

deposits = 0
withdrawals = 0

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == 1:
        balance = balance + amount
        deposits = deposits + amount
        print("Deposit successful")

    elif choice == 2:
        if amount > 10000:
            print("Withdrawal limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
            withdrawals = withdrawals + amount
            print("Withdrawal successful")

    else:
        print("Invalid transaction")

    print("Current Balance:", balance)

print("\n--- Transaction Summary ---")
print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
print("Final Balance:", balance)
