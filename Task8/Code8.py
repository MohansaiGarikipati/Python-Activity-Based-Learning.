
# Integrated University Fee and Eligibility Audit

TOTAL_FEE = 50000
MIN_ATTENDANCE = 75
MIN_INTERNAL_MARKS = 40

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    fee_paid = float(input("Enter Fee Paid: "))
    attendance = float(input("Enter Attendance Percentage: "))
    internal_marks = float(input("Enter Internal Marks (out of 100): "))

    # Validate student details
    if fee_paid < 0 or fee_paid > TOTAL_FEE:
        print("Invalid fee amount. Enter again.")
        continue

    if attendance < 0 or attendance > 100:
        print("Invalid attendance percentage.")
        continue

    if internal_marks < 0 or internal_marks > 100:
        print("Invalid internal marks.")
        continue

    outstanding_fee = TOTAL_FEE - fee_paid
    reasons = []

    if outstanding_fee > 0:
        reasons.append("Outstanding Fee")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Low Attendance")

    if internal_marks < MIN_INTERNAL_MARKS:
        reasons.append("Insufficient Internal Marks")

    if len(reasons) == 0:
        status = "Eligible"
    else:
        status = "Not Eligible"

    student = {
        "roll_no": roll_no,
        "name": name,
        "fee_paid": fee_paid,
        "outstanding_fee": outstanding_fee,
        "attendance": attendance,
        "internal_marks": internal_marks,
        "reasons": reasons,
        "status": status
    }

    students.append(student)

# Display individual student report
print("\n========== STUDENT ELIGIBILITY REPORT ==========")

for s in students:
    print("\nRoll Number:", s["roll_no"])
    print("Name:", s["name"])
    print("Fee Paid: Rs.", s["fee_paid"])
    print("Outstanding Fee: Rs.", s["outstanding_fee"])
    print("Attendance:", s["attendance"], "%")
    print("Internal Marks:", s["internal_marks"])
    print("Status:", s["status"])

    if s["reasons"]:
        print("Reasons:", ", ".join(s["reasons"]))
    else:
        print("Reasons: None")

# Generate reason-wise report
fee_count = 0
attendance_count = 0
marks_count = 0
eligible_count = 0
not_eligible_count = 0

for s in students:
    if s["outstanding_fee"] > 0:
        fee_count += 1

    if s["attendance"] < MIN_ATTENDANCE:
        attendance_count += 1

    if s["internal_marks"] < MIN_INTERNAL_MARKS:
        marks_count += 1

    if s["status"] == "Eligible":
        eligible_count += 1
    else:
        not_eligible_count += 1

print("\n========== REASON-WISE SUMMARY ==========")
print("Students with Outstanding Fee:", fee_count)
print("Students with Low Attendance:", attendance_count)
print("Students with Insufficient Internal Marks:", marks_count)

print("\n========== FINAL SUMMARY ==========")
print("Total Valid Students:", len(students))
print("Eligible Students:", eligible_count)
print("Not Eligible Students:", not_eligible_count)

