
SENIOR_CONCESSION = 10
LOW_INCOME_CONCESSION = 15


def calculate_bill(consultation, diagnostic, treatment, category):
    subtotal = consultation + diagnostic + treatment

    # Apply the appropriate concession
    if category == "senior":
        concession_rate = SENIOR_CONCESSION
    elif category == "low-income":
        concession_rate = LOW_INCOME_CONCESSION
    else:
        concession_rate = 0

    concession = subtotal * concession_rate / 100
    final_bill = subtotal - concession

    return subtotal, concession, final_bill


def classify_patient(final_bill, amount_paid):
    balance = round(final_bill - amount_paid, 2)

    if balance == 0:
        status = "Fully Paid"
    elif amount_paid == 0:
        status = "Unpaid"
    else:
        status = "Partially Paid"

    return balance, status


patients = []

n = int(input("Enter number of patients: "))

if n <= 0:
    print("Number of patients must be positive.")
else:
    for i in range(n):
        print(f"\nEnter details of patient {i + 1}")

        name = input("Enter patient name: ").strip()
        category = input(
            "Enter category (regular/senior/low-income): "
        ).strip().lower()

        if category not in ["regular", "senior", "low-income"]:
            print("Invalid patient category. Skipping patient.")
            continue

        try:
            consultation = float(
                input("Enter consultation charges (Rs.): ")
            )
            diagnostic = float(
                input("Enter diagnostic charges (Rs.): ")
            )
            treatment = float(
                input("Enter treatment charges (Rs.): ")
            )
            amount_paid = float(
                input("Enter amount paid (Rs.): ")
            )
        except ValueError:
            print("Invalid numeric input. Skipping patient.")
            continue
        if min(consultation, diagnostic, treatment, amount_paid) < 0:
            print("Charges and payment cannot be negative.")
            continue

        subtotal, concession, final_bill = calculate_bill(
            consultation, diagnostic, treatment, category
        )

        if amount_paid > final_bill:
            print("Payment cannot exceed the final bill.")
            continue

        balance, status = classify_patient(
            final_bill, amount_paid
        )

        patients.append({
            "name": name,
            "category": category,
            "consultation": consultation,
            "diagnostic": diagnostic,
            "treatment": treatment,
            "subtotal": subtotal,
            "concession": concession,
            "final_bill": final_bill,
            "paid": amount_paid,
            "balance": balance,
            "status": status
        })
    print("\n--- HOSPITAL BILLING REPORT ---")

    for p in patients:
        print(f"\nPatient Name: {p['name']}")
        print(f"Category: {p['category']}")
        print(f"Consultation Charges: Rs. {p['consultation']:.2f}")
        print(f"Diagnostic Charges: Rs. {p['diagnostic']:.2f}")
        print(f"Treatment Charges: Rs. {p['treatment']:.2f}")
        print(f"Subtotal: Rs. {p['subtotal']:.2f}")
        print(f"Concession: Rs. {p['concession']:.2f}")
        print(f"Final Bill: Rs. {p['final_bill']:.2f}")
        print(f"Amount Paid: Rs. {p['paid']:.2f}")
        print(f"Outstanding Balance: Rs. {p['balance']:.2f}")
        print(f"Payment Status: {p['status']}")

