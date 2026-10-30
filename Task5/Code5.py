
ACCEPTABLE_LIMIT = 10

food_records = []

try:
    n = int(input("Enter number of days to monitor: "))

    if n <= 0:
        print("Number of days must be positive.")

    else:
        for i in range(n):
            print(f"\nEnter details for Day {i + 1}")

            day = input("Enter day name: ").strip()

            try:
                prepared = int(input("Enter meals prepared: "))
                served = int(input("Enter meals served: "))
            except ValueError:
                print("Invalid input. Skipping this day.")
                continue
            if prepared <= 0 or served < 0:
                print("Invalid meal quantities. Skipping this day.")
                continue

            if served > prepared:
                print("Meals served cannot exceed meals prepared.")
                continue
            leftover = prepared - served
            wastage = (leftover / prepared) * 100

            if wastage > ACCEPTABLE_LIMIT:
                status = "Excessive Wastage"
            else:
                status = "Acceptable Wastage"

            food_records.append({
                "day": day,
                "prepared": prepared,
                "served": served,
                "leftover": leftover,
                "wastage": wastage,
                "status": status
            })
        print("\n--- DAILY FOOD WASTE REPORT ---")

        for record in food_records:
            print(f"\nDay: {record['day']}")
            print(f"Meals Prepared: {record['prepared']}")
            print(f"Meals Served: {record['served']}")
            print(f"Leftover Meals: {record['leftover']}")
            print(f"Wastage Percentage: {record['wastage']:.2f}%")
            print(f"Status: {record['status']}")
        total_prepared = sum(r["prepared"] for r in food_records)
        total_served = sum(r["served"] for r in food_records)
        total_leftover = sum(r["leftover"] for r in food_records)

        print("\n--- OVERALL FOOD WASTE SUMMARY ---")

        if total_prepared > 0:
            overall_wastage = (
                total_leftover / total_prepared
            ) * 100

            print(f"Total Meals Prepared: {total_prepared}")
            print(f"Total Meals Served: {total_served}")
            print(f"Total Leftover Meals: {total_leftover}")
            print(f"Overall Wastage: {overall_wastage:.2f}%")

            if overall_wastage > ACCEPTABLE_LIMIT:
                print("Warning: Overall food wastage is excessive!")
            else:
                print("Overall food wastage is acceptable.")

        else:
            print("No valid food records available.")

except ValueError:
    print("Please enter a valid number of days.")

