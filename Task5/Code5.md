# Food Waste Monitoring System – Python Project

## 1. Problem Statement

The Food Waste Monitoring System is designed to monitor food preparation, food consumption, and leftover quantities across several days. The system records the number of meals prepared and the number of meals served each day.

## 2. Algorithm

1. Start the program.
2. Set the acceptable food wastage percentage limit to 10%.
3. Input the number of days to monitor.
4. For each day:
   - Enter the day name.
   - Enter the number of meals prepared.
   - Enter the number of meals served.
5. Validate the input values:
   - Meals prepared must be greater than zero.
   - Meals served cannot be negative.
   - Meals served cannot exceed meals prepared.
6. Calculate leftover meals:

&#x20;  Leftover = Meals Prepared − Meals Served

7\. Calculate wastage percentage:

&#x20;  Wastage Percentage = (Leftover / Meals Prepared) × 100

8. Compare the wastage percentage with the acceptable limit.
9. If wastage exceeds 10%, identify that day as having excessive food waste.
10. Store and display the daily food details.
11. Calculate total meals prepared, served, and wasted across all days.
12. Calculate the overall wastage percentage.
13. Display the final food waste monitoring report.
14. Stop the program.

Assumptions:

- Acceptable food wastage limit is 10%.
- Each meal is counted as one unit.
- Meals served cannot exceed meals prepared.
- Invalid daily entries are rejected.

## 3. Flowchart

START

Set acceptable wastage limit (10%)

Input number of days

Enter meals prepared and meals served

Validate input values

Calculate leftover meals and wastage percentage

Is wastage percentage greater than 10%?

Yes

Mark excessive wastage

No

Mark acceptable wastage

Calculate overall food wastage

Display daily and overall report

STOP

## 4. Sample Input

```
Enter number of days to monitor: 4

Enter details for Day 1
Enter day name: Monday
Enter meals prepared: 100
Enter meals served: 90

Enter details for Day 2
Enter day name: Tuesday
Enter meals prepared: 120
Enter meals served: 100

Enter details for Day 3
Enter day name: Wednesday
Enter meals prepared: 150
Enter meals served: 140

Enter details for Day 4
Enter day name: Thursday
Enter meals prepared: 80
Enter meals served: 60
```

## 5. Sample Output

```
--- DAILY FOOD WASTE REPORT ---

Day: Monday
Meals Prepared: 100
Meals Served: 90
Leftover Meals: 10
Wastage Percentage: 10.00%
Status: Acceptable Wastage

Day: Tuesday
Meals Prepared: 120
Meals Served: 100
Leftover Meals: 20
Wastage Percentage: 16.67%
Status: Excessive Wastage

Day: Wednesday
Meals Prepared: 150
Meals Served: 140
Leftover Meals: 10
Wastage Percentage: 6.67%
Status: Acceptable Wastage

Day: Thursday
Meals Prepared: 80
Meals Served: 60
Leftover Meals: 20
Wastage Percentage: 25.00%
Status: Excessive Wastage

--- OVERALL FOOD WASTE SUMMARY ---

Total Meals Prepared: 450
Total Meals Served: 390
Total Leftover Meals: 60
Overall Wastage: 13.33%
Warning: Overall food wastage is excessive!
```

This project demonstrates the practical application of Python variables, arithmetic operations, conditional statements, loops, lists, dictionaries, and exception handling. It helps food-service organizations monitor food consumption and reduce unnecessary food waste.
