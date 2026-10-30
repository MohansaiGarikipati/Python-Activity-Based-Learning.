
# Campus Festival Registration and Financial Audit

REGISTRATION_FEE = 500

participants = []
registration_ids = set()
duplicates = []

# Participant registration
n = int(input("Enter number of participants: "))

for i in range(n):
    print("\nParticipant", i + 1)

    reg_id = input("Enter Registration ID: ")
    name = input("Enter Participant Name: ")

    if reg_id in registration_ids:
        print("Duplicate Registration! Entry rejected.")
        duplicates.append((reg_id, name))
    else:
        registration_ids.add(reg_id)

        participants.append({
            "id": reg_id,
            "name": name
        })

# Calculate registration income
registration_income = len(participants) * REGISTRATION_FEE

# Sponsorship details
sponsors = []
s = int(input("\nEnter number of sponsors: "))

for i in range(s):
    print("\nSponsor", i + 1)

    sponsor_name = input("Enter Sponsor Name: ")
    contribution = float(input("Enter Contribution: Rs. "))

    if contribution < 0:
        print("Invalid amount. Sponsor skipped.")
        continue

    sponsors.append((sponsor_name, contribution))

total_sponsorship = sum(
    amount for name, amount in sponsors
)

# Festival expenses
expenses = []
e = int(input("\nEnter number of expenses: "))

for i in range(e):
    print("\nExpense", i + 1)

    category = input("Enter Expense Category: ")
    amount = float(input("Enter Expense Amount: Rs. "))

    if amount < 0:
        print("Invalid amount. Expense skipped.")
        continue

    expenses.append((category, amount))

total_expenses = sum(
    amount for category, amount in expenses
)

# Financial calculations
total_income = registration_income + total_sponsorship
final_balance = total_income - total_expenses

# Participant report
print("\n========== PARTICIPANT REPORT ==========")

for p in participants:
    print(p["id"], "-", p["name"], "- Accepted")

print("\n========== DUPLICATE REPORT ==========")

if duplicates:
    for reg_id, name in duplicates:
        print(reg_id, "-", name, "- Duplicate")
else:
    print("No duplicate registrations found.")

# Sponsorship report
print("\n========== SPONSORSHIP REPORT ==========")

for name, amount in sponsors:
    print(name, ": Rs.", amount)

print("Total Sponsorship: Rs.", total_sponsorship)

# Expense report
print("\n========== EXPENSE REPORT ==========")

for category, amount in expenses:
    print(category, ": Rs.", amount)

print("Total Expenses: Rs.", total_expenses)

# Final financial audit
print("\n========== FINAL FINANCIAL AUDIT ==========")

print("Total Registration Entries:", n)
print("Valid Registrations:", len(participants))
print("Duplicate Registrations:", len(duplicates))
print("Registration Fee per Participant: Rs.", REGISTRATION_FEE)
print("Registration Income: Rs.", registration_income)
print("Sponsorship Income: Rs.", total_sponsorship)
print("Total Income: Rs.", total_income)
print("Total Expenses: Rs.", total_expenses)
print("Final Financial Balance: Rs.", final_balance)

if final_balance > 0:
    print("Financial Status: SURPLUS")
elif final_balance < 0:
    print("Financial Status: DEFICIT")
else:
    print("Financial Status: BREAK EVEN")

