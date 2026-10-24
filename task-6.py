
n = int(input("Enter number of products: "))
budget = float(input("Enter your budget: "))

names = []
prices = []
qtys = []
total = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    qty = int(input("Enter quantity: "))

    amount = price * qty

    if amount >= 1000:
        amount = amount * 0.90

    names.append(name)
    prices.append(price)
    qtys.append(qty)
    total = total + amount

print("\nOriginal Total:", round(total, 2))

for i in range(n):
    while total > budget and qtys[i] > 0:
        old_amount = prices[i] * qtys[i]

        if old_amount >= 1000:
            old_amount = old_amount * 0.90

        qtys[i] = qtys[i] - 1

        new_amount = prices[i] * qtys[i]

        if new_amount >= 1000:
            new_amount = new_amount * 0.90

        total = total - old_amount + new_amount

        print("Reduced quantity of", names[i])

print("\nFinal Shopping List")

for i in range(n):
    if qtys[i] > 0:
        print(names[i], "- Quantity:", qtys[i])
    else:
        print(names[i], "- Removed")

print("Final Total:", round(total, 2))

if total <= budget:
    print("Shopping is within budget")
else:
    print("Budget cannot be met")
