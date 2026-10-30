# Multi-Stage Scholarship Shortlisting System – Python Project

## 1. Problem Statement

The Multi-Stage Scholarship Shortlisting System is designed to select eligible students for scholarships based on multiple conditions, including academic performance, attendance percentage, and annual family income.

## 2. Algorithm

1. Start the program.
2. Define scholarship eligibility criteria:
   - Minimum aggregate marks: 75%.
   - Minimum subject marks: 60%.
   - Minimum attendance: 75%.
   - Maximum annual family income: ₹2,50,000.
3. Input the number of student applicants.
4. Input the fixed scholarship quota.
5. For each student:
   - Enter the student's name.
   - Enter marks in three subjects.
   - Enter attendance percentage.
   - Enter annual family income.
6. Validate all input values.
7. Calculate the aggregate percentage.
8. Apply the academic eligibility condition.
9. Check the attendance requirement.
10. Check the annual family income condition.
11. Add students satisfying all conditions to the eligible list.
12. Sort eligible students using:
    - Aggregate marks in descending order.
    - Attendance in descending order.
    - Family income in ascending order.
    - Name in alphabetical order.
13. Select students according to the fixed scholarship quota.
14. Classify remaining eligible students as waiting list candidates.
15. Display selected students, waiting list, and rejected applicants.
16. Stop the program.

## 3. Flowchart

START

Initialize eligibility criteria and scholarship quota

Input student details and marks

Validate student information

Check academic eligibility

Check attendance and income conditions

Not eligible

Add to rejected list

Eligible

Add to eligible list

Rank eligible students using tie-breaking rules

Select candidates within scholarship quota

Display selected, waiting list, and rejected students

STOP
```

## 4. Sample Input

```
Enter number of student applicants: 5
Enter scholarship quota: 2

Enter details of Student 1
Enter student name: Rahul
Enter Subject 1 marks: 90
Enter Subject 2 marks: 85
Enter Subject 3 marks: 95
Enter attendance percentage: 90
Enter annual family income (Rs.): 200000

Enter details of Student 2
Enter student name: Priya
Enter Subject 1 marks: 90
Enter Subject 2 marks: 90
Enter Subject 3 marks: 90
Enter attendance percentage: 95
Enter annual family income (Rs.): 220000

Enter details of Student 3
Enter student name: Ravi
Enter Subject 1 marks: 80
Enter Subject 2 marks: 70
Enter Subject 3 marks: 75
Enter attendance percentage: 80
Enter annual family income (Rs.): 250000

Enter details of Student 4
Enter student name: Anu
Enter Subject 1 marks: 90
Enter Subject 2 marks: 55
Enter Subject 3 marks: 85
Enter attendance percentage: 90
Enter annual family income (Rs.): 150000

Enter details of Student 5
Enter student name: Kiran
Enter Subject 1 marks: 85
Enter Subject 2 marks: 80
Enter Subject 3 marks: 90
Enter attendance percentage: 70
Enter annual family income (Rs.): 180000
```

## 5. Sample Output

```
--- SELECTED SCHOLARSHIP CANDIDATES ---

Rank: 1
Name: Priya
Aggregate: 90.00%
Attendance: 95.00%
Annual Income: Rs. 220000.00
Status: Scholarship Selected

Rank: 2
Name: Rahul
Aggregate: 90.00%
Attendance: 90.00%
Annual Income: Rs. 200000.00
Status: Scholarship Selected

--- WAITING LIST ---

3. Ravi - Aggregate: 75.00%

--- REJECTED STUDENTS ---

Anu: Academic criteria not satisfied
Kiran: Attendance below minimum

--- FINAL SUMMARY ---
Total Applicants: 5
Eligible Applicants: 3
Scholarship Quota: 2
Selected Students: 2
Waiting List Students: 1
Rejected Students: 2
```

This project demonstrates the practical application of Python variables, lists, dictionaries, loops, conditional statements, sorting techniques, exception handling, and arithmetic operations. It helps universities conduct a fair, transparent, and systematic scholarship selection process.
