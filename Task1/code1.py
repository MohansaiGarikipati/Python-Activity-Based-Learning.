
students = []
eligible_students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    name = input("Enter student name: ")
    m1 = float(input("Enter marks in Subject 1 (out of 100): "))
    m2 = float(input("Enter marks in Subject 2 (out of 100): "))
    m3 = float(input("Enter marks in Subject 3 (out of 100): "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income (Rs.): "))
    if not all(0 <= m <= 100 for m in [m1, m2, m3]):
        print("Invalid subject marks. Skipping student.")
        continue

    if not 0 <= attendance <= 100 or income < 0:
        print("Invalid attendance or income. Skipping student.")
        continue

    aggregate = (m1 + m2 + m3) / 3

    student = {
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "eligible": (
            aggregate >= MIN_AGGREGATE
            and min(m1, m2, m3) >= MIN_SUBJECT_MARK
            and attendance >= MIN_ATTENDANCE
            and income <= MAX_INCOME
        )
    }

    students.append(student)

    if student["eligible"]:
        eligible_students.append(students)
eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

print("\n--- STUDENT ELIGIBILITY RESULTS ---")

for s in students:
    status = "Eligible" if s["eligible"] else "Not Eligible"
    print(f"{s['name']}: {status} "
          f"(Aggregate: {s['aggregate']:.2f}%)")

print("\n--- SCHOLARSHIP MERIT LIST ---")

if eligible_students:
    for rank, s in enumerate(eligible_students, start=1):
        print(
            f"{rank}. {s['name']} | "
            f"Aggregate: {s['aggregate']:.2f}% | "
            f"Attendance: {s['attendance']:.1f}% | "
            f"Income: Rs. {s['income']:.0f}"
        )
else:
    print("No eligible students found.")

