
# Smart Hostel Resource Monitoring

ELECTRICITY_RATE = 6
WATER_RATE = 10

MAX_ELECTRICITY = 200
MAX_WATER = 30

floors = []

n = int(input("Enter number of floors: "))

if n <= 0:
    print("Number of floors must be positive.")

else:
    for i in range(n):
        print("\nEnter details for Floor", i + 1)

        rooms_count = int(input("Enter number of rooms: "))

        if rooms_count <= 0:
            print("Invalid number of rooms.")
            continue

        rooms = []

        for j in range(rooms_count):
            print("\nRoom", j + 1)

            room_no = input("Enter room number: ")
            electricity = float(
                input("Enter electricity consumption (units): ")
            )
            water = float(
                input("Enter water consumption (units): ")
            )

            if electricity < 0 or water < 0:
                print("Invalid consumption. Room skipped.")
                continue

            electricity_charge = electricity * ELECTRICITY_RATE
            water_charge = water * WATER_RATE
            total_charge = electricity_charge + water_charge

            violations = []

            if electricity > MAX_ELECTRICITY:
                violations.append("High Electricity Usage")

            if water > MAX_WATER:
                violations.append("High Water Usage")

            room = {
                "room_no": room_no,
                "electricity": electricity,
                "water": water,
                "electricity_charge": electricity_charge,
                "water_charge": water_charge,
                "total_charge": total_charge,
                "violations": violations
            }

            rooms.append(room)

        floors.append(rooms)

    # Room-wise report
    print("\n========== ROOM-WISE REPORT ==========")

    for i, rooms in enumerate(floors):
        print("\nFloor", i + 1)

        for room in rooms:
            print("\nRoom Number:", room["room_no"])
            print("Electricity:", room["electricity"], "units")
            print("Water:", room["water"], "units")
            print("Electricity Charge: Rs.",
                  room["electricity_charge"])
            print("Water Charge: Rs.", room["water_charge"])
            print("Total Charge: Rs.", room["total_charge"])

            if room["violations"]:
                print("Violation:", ", ".join(room["violations"]))
            else:
                print("Status: Within Limits")

    # Floor-wise analysis
    print("\n========== FLOOR-WISE ANALYSIS ==========")

    highest_electricity = -1
    highest_water = -1
    electricity_floor = 0
    water_floor = 0

    for i, rooms in enumerate(floors):
        total_electricity = sum(
            room["electricity"] for room in rooms
        )

        total_water = sum(
            room["water"] for room in rooms
        )

        total_charge = sum(
            room["total_charge"] for room in rooms
        )

        print("\nFloor", i + 1)
        print("Total Electricity:", total_electricity, "units")
        print("Total Water:", total_water, "units")
        print("Total Charges: Rs.", total_charge)

        if total_electricity > highest_electricity:
            highest_electricity = total_electricity
            electricity_floor = i + 1

        if total_water > highest_water:
            highest_water = total_water
            water_floor = i + 1

    print("\n========== RESOURCE COMPARISON ==========")

    if floors:
        print("Highest Electricity Usage: Floor",
              electricity_floor)
        print("Highest Water Usage: Floor", water_floor)

    print("\nMonitoring Report Generated Successfully.")

