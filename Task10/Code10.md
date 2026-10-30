# Project: Campus Festival Registration and Financial Audit

## 1. Problem Statement

The Campus Festival Registration and Financial Audit system is designed to manage participant registrations, registration fees, sponsorship contributions, and festival 

## 2. Algorithm

1. Start the program.
2. Enter the number of participants.
3. Read participant names and registration IDs.
4. Check each registration ID for duplicates.
5. Accept unique registrations and reject duplicate entries.
6. Calculate the total registration fee.
7. Enter sponsor names and contribution amounts.
8. Calculate the total sponsorship contribution.
9. Enter festival expense categories and amounts.
10. Calculate the total festival expenses.
11. Calculate total income.
12. Calculate the final financial balance.
13. Display participant registration details.
14. Display duplicate registration details.
15. Display sponsorship and expense reports.
16. Display the final financial balance.
17. Stop the program.

## 3. Flowchart

START

Enter participant registration details

Check duplicate registration IDs

Duplicate ID

Reject registration

Unique ID

Accept registration

Calculate registration fees and sponsorship income

Enter and calculate festival expenses

Calculate final financial balance

Generate final audit report

STOP


## 4. Sample Input

```
Enter number of participants: 4

Participant 1
Registration ID: P101
Participant Name: Ravi

Participant 2
Registration ID: P102
Participant Name: Suresh

Participant 3
Registration ID: P103
Participant Name: Priya

Participant 4
Registration ID: P102
Participant Name: Kiran

Enter number of sponsors: 2

Sponsor 1
Sponsor Name: ABC Company
Contribution: 10000

Sponsor 2
Sponsor Name: XYZ Company
Contribution: 15000

Enter number of expenses: 3

Expense 1
Expense Category: Decoration
Expense Amount: 5000

Expense 2
Expense Category: Food
Expense Amount: 8000

Expense 3
Expense Category: Sound System
Expense Amount: 4000
```

## 5. Sample Output

```
Duplicate Registration! Entry rejected.

========== PARTICIPANT REPORT ==========

P101 - Ravi - Accepted
P102 - Suresh - Accepted
P103 - Priya - Accepted

========== DUPLICATE REPORT ==========

P102 - Kiran - Duplicate

========== SPONSORSHIP REPORT ==========

ABC Company : Rs. 10000
XYZ Company : Rs. 15000
Total Sponsorship: Rs. 25000

========== EXPENSE REPORT ==========

Decoration : Rs. 5000
Food : Rs. 8000
Sound System : Rs. 4000
Total Expenses: Rs. 17000

========== FINAL FINANCIAL AUDIT ==========

Total Registration Entries: 4
Valid Registrations: 3
Duplicate Registrations: 1
Registration Fee per Participant: Rs. 500
Registration Income: Rs. 1500
Sponsorship Income: Rs. 25000
Total Income: Rs. 26500
Total Expenses: Rs. 17000
Final Financial Balance: Rs. 9500
Financial Status: SURPLUS
