
entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))

if entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("Invalid time")

else:
    vehicle = input("Enter vehicle type (bike/car): ")

    if exit < entry:
        hours = 24 - entry + exit
        overnight = True
    else:
        hours = exit - entry
        overnight = False

    if hours == 0:
        hours = 1

    if vehicle == "bike":
        rate = 10
    elif vehicle == "car":
        rate = 20
    else:
        rate = 0
        print("Invalid vehicle type")

    if rate > 0:
        fee = hours * rate

        if overnight:
            fee = fee + 50

        if fee > 300:
            fee = 300

        if hours > 12:
            fee = fee + 50

        print("Parking Hours:", hours)
        print("Overnight Parking:", overnight)
        print("Total Parking Fee: Rs.", fee)
