# Project: Integrated University Fee and Eligibility Audit

## 1. Problem Statement

The Integrated University Fee and Eligibility Audit system is designed to check students' fee payments, attendance, internal marks, and examination eligibility. It identifies students who have outstanding fees or do not meet the required attendance and internal marks criteria.

## 2. Algorithm

1. Start the program.
2. Enter the number of students.
3. For each student, enter:
   - Student name and roll number.
   - Total semester fee.
   - Fee amount paid.
   - Attendance percentage.
   - Internal marks.
4. Calculate the outstanding fee.
5. Check whether the fee is fully paid.
6. Check whether attendance is at least 75%.
7. Check whether internal marks are at least 40.
8. If all conditions are satisfied, mark the student as eligible.
9. Otherwise, display all outstanding conditions.
10. Generate a reason-wise report.
11. Stop the program.

## 3. Flowchart

START

Enter student details, fee payment, attendance and internal marks

Calculate outstanding fee

Check fee, attendance ≥ 75% and internal marks ≥ 40

All conditions satisfied

Eligible

One or more conditions failed

Not Eligible

Generate reason-wise report

STOP

## 4. Sample Input

```
Enter number of students: 3

Student 1:
Roll Number: 101
Student Name: Ravi
Fee Paid: 50000
Attendance: 82
Internal Marks: 75

Student 2:
Roll Number: 102
Student Name: Suresh
Fee Paid: 40000
Attendance: 68
Internal Marks: 55

Student 3:
Roll Number: 103
Student Name: Priya
Fee Paid: 50000
Attendance: 80
Internal Marks: 32
```

## 5. Sample Output

```
========== STUDENT ELIGIBILITY REPORT ==========

Roll Number: 101
Name: Ravi
Fee Paid: Rs. 50000
Outstanding Fee: Rs. 0
Attendance: 82 %
Internal Marks: 75
Status: Eligible
Reasons: None

Roll Number: 102
Name: Suresh
Fee Paid: Rs. 40000
Outstanding Fee: Rs. 10000
Attendance: 68 %
Internal Marks: 55
Status: Not Eligible
Reasons: Outstanding Fee, Low Attendance

Roll Number: 103
Name: Priya
Fee Paid: Rs. 50000
Outstanding Fee: Rs. 0
Attendance: 80 %
Internal Marks: 32
Status: Not Eligible
Reasons: Insufficient Internal Marks

========== REASON-WISE SUMMARY ==========

Students with Outstanding Fee: 1
Students with Low Attendance: 1
Students with Insufficient Internal Marks: 1

========== FINAL SUMMARY ==========

Total Valid Students: 3
Eligible Students: 1
Not Eligible Students: 2
