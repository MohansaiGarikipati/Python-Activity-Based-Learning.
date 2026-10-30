# Multi-Branch Expense Matrix Analysis – Python Project

## 1. Problem Statement

The Multi-Branch Expense Matrix Analysis System is designed to analyze monthly expenses of different branches of an organization across multiple expense categories.

The system uses nested lists (matrices) to store expense details such as salaries, electricity bills, maintenance, transportation, and other expenses for each branch.

It calculates the total expenses of each branch, category-wise expenses, and average expenses. It also identifies the branch and expense category that contribute the largest amount to the overall expenditure.

This system helps organizations monitor their spending, compare branch performance, identify major expenditure areas, and improve financial planning.

## 2. Algorithm

1. Start the program.
2. Input the number of branches and expense categories.
3. Input the names of all branches.
4. Input the names of all expense categories.
5. Create a nested list (matrix) to store monthly expenses.
6. For each branch:
   - Enter the expense amount for every category.
   - Validate that all expense values are non-negative.
7. Calculate the total expenses for each branch by adding all category expenses.
8. Calculate the total expenses for each category across all branches.
9. Calculate the average expense for each branch.
10. Calculate the average expense for each category.
11. Identify the branch with the highest total expenditure.
12. Identify the category with the highest total expenditure.
13. Calculate the overall organizational expenditure.
14. Display the expense matrix, totals, averages, and largest contributors.
15. Stop the program.

## 3. Flowchart

START

Input number of branches and expense categories

Enter branch names and category names

Create nested list to store expenses

Input and validate monthly expenses

Calculate branch-wise and category-wise totals

Calculate average expenses

Identify highest expenditure branch and category

Display expense analysis report

STOP

## 4. Sample Input

```
Enter number of branches: 3
Enter number of expense categories: 4

Enter branch 1 name: Hyderabad
Enter branch 2 name: Vijayawada
Enter branch 3 name: Guntur

Enter expense category 1: Salaries
Enter expense category 2: Electricity
Enter expense category 3: Maintenance
Enter expense category 4: Transport

Enter expenses for Hyderabad
Enter Salaries expense: Rs. 50000
Enter Electricity expense: Rs. 10000
Enter Maintenance expense: Rs. 5000
Enter Transport expense: Rs. 8000

Enter expenses for Vijayawada
Enter Salaries expense: Rs. 60000
Enter Electricity expense: Rs. 12000
Enter Maintenance expense: Rs. 7000
Enter Transport expense: Rs. 9000

Enter expenses for Guntur
Enter Salaries expense: Rs. 45000
Enter Electricity expense: Rs. 15000
Enter Maintenance expense: Rs. 6000
Enter Transport expense: Rs. 10000
```

## 5. Sample Output

```
--- EXPENSE MATRIX ---

Branch      Salaries  Electricity  Maintenance  Transport
Hyderabad   50000     10000        5000         8000
Vijayawada  60000     12000        7000         9000
Guntur      45000     15000        6000         10000

--- BRANCH-WISE ANALYSIS ---

Branch: Hyderabad
Total Expense: Rs. 73000.00
Average Expense: Rs. 18250.00

Branch: Vijayawada
Total Expense: Rs. 88000.00
Average Expense: Rs. 22000.00

Branch: Guntur
Total Expense: Rs. 76000.00
Average Expense: Rs. 19000.00

--- CATEGORY-WISE ANALYSIS ---

Category: Salaries
Total Expense: Rs. 155000.00
Average Expense: Rs. 51666.67

Category: Electricity
Total Expense: Rs. 37000.00
Average Expense: Rs. 12333.33

Category: Maintenance
Total Expense: Rs. 18000.00
Average Expense: Rs. 6000.00

Category: Transport
Total Expense: Rs. 27000.00
Average Expense: Rs. 9000.00

--- OVERALL EXPENSE SUMMARY ---

Total Organizational Expense: Rs. 237000.00
Highest Spending Branch: Vijayawada
Highest Spending Category: Salaries
```

This project demonstrates the practical application of Python nested lists, loops, indexing, conditional statements, built-in functions, and arithmetic operations. It helps organizations monitor expenses and make better financial decisions.
