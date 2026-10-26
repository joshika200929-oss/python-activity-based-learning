
n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    category = input("Enter category (food/clothes/electronics): ")

    amount = price * qty

    if category == "food":
        tax = amount * 0.05
    elif category == "clothes":
        tax = amount * 0.10
    else:
        tax = amount * 0.18

    if amount >= 5000:
        discount = amount * 0.20
    elif amount >= 2000:
        discount = amount * 0.10
    else:
        discount = 0

    if discount > 1000:
        discount = 1000

    final = amount + tax - discount
    total = total + final

    print("\nProduct:", name)
    print("Amount:", amount)
    print("Tax:", round(tax, 2))
    print("Discount:", round(discount, 2))
    print("Final Price:", round(final, 2))

print("\nTotal Bill: Rs.", round(total, 2))
