
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per participant: "))

fixed_cost = venue + equipment + transport
variable_cost = participants * (catering + certificate)
total_cost = fixed_cost + variable_cost

contribution = participants * fee
total_funds = contribution + sponsorship
shortfall = total_cost - total_funds

print("\n--- Event Financial Report ---")
print("Fixed Cost:", fixed_cost)
print("Variable Cost:", variable_cost)
print("Total Cost:", total_cost)
print("Participant Contributions:", contribution)
print("Sponsorship:", sponsorship)

if shortfall > 0:
    print("Sponsorship Shortfall:", shortfall)
else:
    print("Surplus Amount:", abs(shortfall))
if fee > catering + certificate:
    required = (fixed_cost - sponsorship) / (fee - catering - certificate)

    if required < 0:
        required = 0

    print("Minimum Registrations to Break Even:", int(required) + (required % 1 > 0))
else:
    print("Break-even is not possible with this registration fee.")
