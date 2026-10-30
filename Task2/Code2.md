# Progressive Electricity Billing System – Python Project

## 1. Problem Statement

The Progressive Electricity Billing System is designed to calculate household electricity bills based on monthly electricity consumption. The system applies different electricity rates to multiple consumption slabs, along with fixed charges, surcharges, and rebates where applicable.

## 2. Algorithm

1. Start the program.
2. Define the electricity consumption slabs and their rates.
3. Define the fixed charge, surcharge percentage, and rebate percentage.
4. Input the number of months to analyze.
5. For each month:
   - Input the month name and electricity consumption in units (kWh).
   - Calculate the energy charge using progressive slabs.
   - Add the fixed charge.
   - Calculate the surcharge on the energy charge and fixed charge.
   - Apply a rebate if the total before rebate exceeds the specified threshold.
   - Calculate the final bill.
6. Store each month's consumption and bill amount.
7. Compare each month's bill with the previous month's bill.
8. Calculate the percentage increase or decrease.
9. If the bill increases by more than 25%, flag it as an unusual increase.
10. Display the monthly bills, comparisons, and unusual increases.
11. Stop the program.

## 3. Flowchart

START

Initialize slab rates, fixed charges, surcharge and rebate

Input number of months and monthly consumption

Calculate progressive energy charges

Add fixed charge and calculate surcharge

Check rebate eligibility and calculate final bill

Store bill and compare with previous month

Is bill increase greater than 25%?

Yes

Flag unusual increase

No

Record normal change

Display monthly bills and comparison report

STOP

## 4. Sample Input

```
Enter number of months: 3

Month 1
Enter month name: January
Enter electricity consumption (units): 150

Month 2
Enter month name: February
Enter electricity consumption (units): 250

Month 3
Enter month name: March
Enter electricity consumption (units): 400
```

## 5. Sample Output

```
--- MONTHLY ELECTRICITY BILL REPORT ---

Month: January
Consumption: 150.0 units
Energy charge: Rs. 350.00
Fixed charge: Rs. 50.00
Surcharge: Rs. 20.00
Rebate: Rs. 0.00
Final bill: Rs. 420.00

Month: February
Consumption: 250.0 units
Energy charge: Rs. 750.00
Fixed charge: Rs. 50.00
Surcharge: Rs. 40.00
Rebate: Rs. 0.00
Final bill: Rs. 840.00

Month: March
Consumption: 400.0 units
Energy charge: Rs. 1500.00
Fixed charge: Rs. 50.00
Surcharge: Rs. 77.50
Rebate: Rs. 0.00
Final bill: Rs. 1627.50

--- MONTHLY BILL COMPARISON ---

January to February
Bill difference: Rs. 420.00
Percentage change: 100.00%
Warning: Unusual increase in electricity bill!

February to March
Bill difference: Rs. 787.50
Percentage change: 93.75%
Warning:unusual increase in elecricity bill!
