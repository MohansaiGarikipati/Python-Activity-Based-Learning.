# Project: Smart Hostel Resource Monitoring

## 1. Problem Statement

The Smart Hostel Resource Monitoring system is designed to monitor electricity and water consumption in different hostel rooms. It calculates room-wise electricity and water charges, identifies rooms that exceed the permitted consumption limits, and compares resource utilization across different floors.

## 2. Algorithm

1. Start the program.
2. Enter the number of hostel floors.
3. Enter the number of rooms on each floor.
4. For every room, enter:
   - Room number.
   - Electricity consumption in units.
   - Water consumption in units.
5. Calculate electricity charges.
6. Calculate water charges.
7. Calculate the total room charge.
8. Check whether electricity consumption exceeds 200 units.
9. Check whether water consumption exceeds 30 units.
10. Display threshold violations, if any.
11. Calculate total electricity and water consumption for each floor.
12. Compare resource utilization across floors.
13. Display the final monitoring report.
14. Stop the program.

## 3. Flowchart

START

Enter number of floors and rooms

Enter room-wise electricity and water consumption

Calculate electricity charges, water charges and total charges

Check electricity and water consumption limits

Limit exceeded

Display violation

Within limits

Display normal

Calculate and compare floor-wise consumption

Generate final monitoring report

STOP

```

## 4. Sample Input

For this example, there are two floors with two rooms each.

```
Enter number of floors: 2

Enter details for Floor 1
Enter number of rooms: 2

Room 1
Enter room number: 101
Enter electricity consumption: 150
Enter water consumption: 20

Room 2
Enter room number: 102
Enter electricity consumption: 250
Enter water consumption: 35

Enter details for Floor 2
Enter number of rooms: 2

Room 1
Enter room number: 201
Enter electricity consumption: 180
Enter water consumption: 25

Room 2
Enter room number: 202
Enter electricity consumption: 120
Enter water consumption: 15
```

## 5. Sample Output

```
========== ROOM-WISE REPORT ==========

Floor 1

Room Number: 101
Electricity: 150 units
Water: 20 units
Electricity Charge: Rs. 900
Water Charge: Rs. 200
Total Charge: Rs. 1100
Status: Within Limits

Room Number: 102
Electricity: 250 units
Water: 35 units
Electricity Charge: Rs. 1500
Water Charge: Rs. 350
Total Charge: Rs. 1850
Violation: High Electricity Usage, High Water Usage

Floor 2

Room Number: 201
Electricity: 180 units
Water: 25 units
Electricity Charge: Rs. 1080
Water Charge: Rs. 250
Total Charge: Rs. 1330
Status: Within Limits

Room Number: 202
Electricity: 120 units
Water: 15 units
Electricity Charge: Rs. 720
Water Charge: Rs. 150
Total Charge: Rs. 870
Status: Within Limits

========== FLOOR-WISE ANALYSIS ==========

Floor 1
Total Electricity: 400 units
Total Water: 55 units
Total Charges: Rs. 2950

Floor 2
Total Electricity: 300 units
Total Water: 40 units
Total Charges: Rs. 2200

========== RESOURCE COMPARISON ==========

Highest Electricity Usage: Floor 1
Highest Water Usage: Floor 1

Monitoring Report Generated Successfully.
```
