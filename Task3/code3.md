# Hospital Billing and Patient Classification System – Python Project

## 1. Problem Statement

The Hospital Billing and Patient Classification System is designed to calculate the total medical bill for patients based on consultation charges, diagnostic test charges, and treatment charges. The system applies conditional concessions according to patient category and validates billing details to ensure that the entered charges and payments are valid.

## 2. Algorithm

1. Start the program.
2. Define the consultation charge, diagnostic charges, treatment charges, and concession rules.
3. Input the number of patients.
4. For each patient:
   - Enter the patient's name and category.
   - Enter consultation, diagnostic, and treatment charges.
   - Enter the amount paid.
5. Validate that all charges and payment amounts are non-negative.
6. Calculate the subtotal by adding consultation, diagnostic, and treatment charges.
7. Apply the appropriate concession:
   - Senior citizens receive a 10% concession.
   - Eligible low-income patients receive a 15% concession.
   - Other patients receive no concession.
8. Calculate the final bill after subtracting the concession.
9. Validate that the amount paid does not exceed the final bill.
10. Calculate the outstanding balance.
11. Classify the patient's payment status:
    - Fully Paid: outstanding balance is zero.
    - Partially Paid: payment is greater than zero but less than the final bill.
    - Unpaid: no payment has been made.
12. Display the bill details and payment classification.
13. Repeat for all patients.
14. Stop the program.

Assumptions: The concession rates and eligibility rules below are illustrative for this academic project, not official hospital policies. Senior citizens receive a 10% concession, and low-income patients receive a 15% concession. If both categories apply, only the higher concession is used.

## 3. Flowchart

START

Initialize billing and concession rules

Input patient details and medical charges

Validate charges and payment amount

Calculate subtotal and applicable concession

Calculate final bill and outstanding balance

Classify payment status

Paid in full

Fully Paid

Some payment

Partially Paid

No payment

Unpaid

Display patient bill and payment status

STOP

## 4. Sample Input

```
Enter number of patients: 3

Enter details of patient 1
Enter patient name: Ramesh
Enter category (regular/senior/low-income): regular
Enter consultation charges (Rs.): 500
Enter diagnostic charges (Rs.): 1500
Enter treatment charges (Rs.): 3000
Enter amount paid (Rs.): 5000

Enter details of patient 2
Enter patient name: Sita
Enter category (regular/senior/low-income): senior
Enter consultation charges (Rs.): 600
Enter diagnostic charges (Rs.): 1000
Enter treatment charges (Rs.): 4000
Enter amount paid (Rs.): 3000

Enter details of patient 3
Enter patient name: Kiran
Enter category (regular/senior/low-income): low-income
Enter consultation charges (Rs.): 400
Enter diagnostic charges (Rs.): 600
Enter treatment charges (Rs.): 1000
Enter amount paid (Rs.): 0
```

## 5. Sample Output

```
--- HOSPITAL BILLING REPORT ---

Patient Name: Ramesh
Category: regular
Consultation Charges: Rs. 500.00
Diagnostic Charges: Rs. 1500.00
Treatment Charges: Rs. 3000.00
Subtotal: Rs. 5000.00
Concession: Rs. 0.00
Final Bill: Rs. 5000.00
Amount Paid: Rs. 5000.00
Outstanding Balance: Rs. 0.00
Payment Status: Fully Paid

Patient Name: Sita
Category: senior
Consultation Charges: Rs. 600.00
Diagnostic Charges: Rs. 1000.00
Treatment Charges: Rs. 4000.00
Subtotal: Rs. 5600.00
Concession: Rs. 560.00
Final Bill: Rs. 5040.00
Amount Paid: Rs. 3000.00
Outstanding Balance: Rs. 2040.00
Payment Status: Partially Paid

Patient Name: Kiran
Category: low-income
Consultation Charges: Rs. 400.00
Diagnostic Charges: Rs. 600.00
Treatment Charges: Rs. 1000.00
Subtotal: Rs. 2000.00
Concession: Rs. 300.00
Final Bill: Rs. 1700.00
Amount Paid: Rs. 0.00
Outstanding Balance: Rs. 1700.00
Payment Status: Unpaid
- Ramesh: A regular classifies patients according to their payment status. It demonstrates the use of Python functions, conditional statements, loops, exception handling, lists, dictionaries, and arithmetic operations to solve a practical hospital management problem.
