
FIXED_CHARGE = 50
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.05
REBATE_THRESHOLD = 2000
INCREASE_LIMIT = 25

def calculate_energy_charge(units):
    """Calculate charge using progressive consumption slabs."""
    charge = 0

    # First 100 units at Rs. 2 per unit
    charge += min(units, 100) * 2

    # Units from 101 to 200 at Rs. 3 per unit
    if units > 100:
        charge += min(units - 100, 100) * 3

    # Units from 201 to 500 at Rs. 5 per unit
    if units > 200:
        charge += min(units - 200, 300) * 5

    # Units above 500 at Rs. 7 per unit
    if units > 500:
        charge += (units - 500) * 7

    return charge


def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)
    subtotal = energy_charge + FIXED_CHARGE
    surcharge = subtotal * SURCHARGE_RATE
    bill_before_rebate = subtotal + surcharge

    rebate = 0
    if bill_before_rebate > REBATE_THRESHOLD:
        rebate = bill_before_rebate * REBATE_RATE

    final_bill = bill_before_rebate - rebate

    return energy_charge, surcharge, rebate, final_bill
bills = []
n = int(input("Enter number of months: "))

if n <= 0:
    print("Number of months must be positive.")
else:
    for i in range(n):
        print(f"\nMonth {i + 1}")
        month = input("Enter month name: ")
        units = float(input("Enter electricity consumption (units): "))

        if units < 0:
            print("Invalid consumption. Please enter again.")
            continue

        energy, surcharge, rebate, total = calculate_bill(units)

        bills.append({
            "month": month,
            "units": units,
            "energy": energy,
            "surcharge": surcharge,
            "rebate": rebate,
            "total": total
        })

    print("\n--- MONTHLY ELECTRICITY BILL REPORT ---")

    for b in bills:
        print(f"\nMonth: {b['month']}")
        print(f"Consumption: {b['units']:.1f} units")
        print(f"Energy charge: Rs. {b['energy']:.2f}")
        print(f"Fixed charge: Rs. {FIXED_CHARGE:.2f}")
        print(f"Surcharge: Rs. {b['surcharge']:.2f}")
        print(f"Rebate: Rs. {b['rebate']:.2f}")
        print(f"Final bill: Rs. {b['total']:.2f}")

    print("\n--- MONTHLY BILL COMPARISON ---")

    for i in range(1, len(bills)):
        previous = bills[i - 1]["total"]
        current = bills[i]["total"]

        difference = current - previous

        if previous > 0:
            percentage = (difference / previous) * 100
        else:
            percentage = 0

        print(f"\n{bills[i - 1]['month']} to {bills[i]['month']}")
        print(f"Bill difference: Rs. {difference:.2f}")
        print(f"Percentage change: {percentage:.2f}%")

        if percentage > INCREASE_LIMIT:
            print("Warning: Unusual increase in electricity bill!")
        elif percentage < 0:
            print("Electricity bill decreased.")
        else:
            print("No unusual increase detected.")

