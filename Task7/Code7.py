
# Multi-Stage Scholarship Shortlisting System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = []
eligible_students = []
rejected_students = []

try:
    n = int(input("Enter number of student applicants: "))
    quota = int(input("Enter scholarship quota: "))

    if n <= 0 or quota < 0:
        print("Invalid number of applicants or quota.")

    else:
        for i in range(n):
            print(f"\nEnter details of Student {i + 1}")

            name = input("Enter student name: ").strip()

            try:
                m1 = float(input("Enter Subject 1 marks: "))
                m2 = float(input("Enter Subject 2 marks: "))
                m3 = float(input("Enter Subject 3 marks: "))
                attendance = float(
                    input("Enter attendance percentage: ")
                )
                income = float(
                    input("Enter annual family income (Rs.): ")
                )
            except ValueError:
                print("Invalid input. Skipping student.")
                continue

            # Validate input values
            if not name or not all(
                0 <= m <= 100 for m in [m1, m2, m3]
            ) or not 0 <= attendance <= 100 or income < 0:
                print("Invalid student details. Skipping student.")
                continue

            aggregate = (m1 + m2 + m3) / 3

            # Stage 1: Academic eligibility
            academic = (
                aggregate >= MIN_AGGREGATE
                and min(m1, m2, m3) >= MIN_SUBJECT_MARK
            )

            # Stage 2: Attendance eligibility
            attendance_ok = attendance >= MIN_ATTENDANCE

            # Stage 3: Income eligibility
            income_ok = income <= MAX_INCOME

            student = {
                "name": name,
                "aggregate": aggregate,
                "attendance": attendance,
                "income": income
            }

            students.append(student)

            if academic and attendance_ok and income_ok:
                eligible_students.append(student)
            else:
                reasons = []

                if not academic:
                    reasons.append("Academic criteria not satisfied")
                if not attendance_ok:
                    reasons.append("Attendance below minimum")
                if not income_ok:
                    reasons.append("Family income exceeds limit")

                student["reason"] = ", ".join(reasons)
                rejected_students.append(student)

        # Stage 4: Rank eligible students
        eligible_students.sort(
            key=lambda s: (
                -s["aggregate"],
                -s["attendance"],
                s["income"],
                s["name"].lower()
            )
        )

        # Select students according to quota
        selected = eligible_students[:quota]
        waiting_list = eligible_students[quota:]

        # Display selected candidates
        print("\n--- SELECTED SCHOLARSHIP CANDIDATES ---")

        if selected:
            for rank, s in enumerate(selected, start=1):
                print(f"\nRank: {rank}")
                print(f"Name: {s['name']}")
                print(f"Aggregate: {s['aggregate']:.2f}%")
                print(f"Attendance: {s['attendance']:.2f}%")
                print(f"Annual Income: Rs. {s['income']:.2f}")
                print("Status: Scholarship Selected")
        else:
            print("No students selected.")

        # Display waiting list
        print("\n--- WAITING LIST ---")

        if waiting_list:
            for rank, s in enumerate(
                waiting_list, start=len(selected) + 1
            ):
                print(
                    f"{rank}. {s['name']} - "
                    f"Aggregate: {s['aggregate']:.2f}%"
                )
        else:
            print("No students in waiting list.")

        # Display rejected students
        print("\n--- REJECTED STUDENTS ---")

        if rejected_students:
            for s in rejected_students:
                print(f"{s['name']}: {s['reason']}")
        else:
            print("No rejected students.")

        print("\n--- FINAL SUMMARY ---")
        print(f"Total Applicants: {len(students)}")
        print(f"Eligible Applicants: {len(eligible_students)}")
        print(f"Scholarship Quota: {quota}")
        print(f"Selected Students: {len(selected)}")
        print(f"Waiting List Students: {len(waiting_list)}")
        print(f"Rejected Students: {len(rejected_students)}")

except ValueError:
    print("Please enter valid numeric values.")

