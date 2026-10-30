# University Scholarship Allocation System – Python Project

## 1. Problem Statement

The University Scholarship Allocation System is designed to evaluate student applications based on aggregate marks, subject-wise minimum marks, attendance percentage, and annual family income. The system identifies eligible students who satisfy all the scholarship criteria and ranks them according to their aggregate marks.

## 2. Algorithm

1. Start the program.
2. Set the scholarship eligibility criteria:
   - Minimum aggregate marks: 75%.
   - Minimum marks in each subject: 60%.
   - Minimum attendance: 75%.
   - Maximum annual family income: ₹2,50,000.
3. Read the number of student applicants.
4. For each student, input the name, marks in three subjects, attendance percentage, and annual family income.
5. Calculate aggregate percentage using the average of the three subject marks.
6. Check whether the student satisfies all four eligibility conditions.
7. Store eligible students in a separate list.
8. Sort eligible students by:
   - Aggregate percentage in descending order.
   - Attendance in descending order.
   - Annual family income in ascending order.
   - Name in alphabetical order.
9. Display each student's eligibility status.
10. Display the ranked merit list of eligible students.
11. Stop the program.

## 3. Flowchart

START

Set eligibility criteria

Input number of students and student details

Calculate aggregate percentage

Check eligibility criteria

No

Mark as Not Eligible

Yes

Add to eligible list

Sort eligible students using tie-breaking rules

Display eligibility results and merit list

STOP
## 4. Sample Input

```
Enter number of students: 4

Enter details of student 1
Enter student name: Rahul
Enter marks in Subject 1 (out of 100): 90
Enter marks in Subject 2 (out of 100): 85
Enter marks in Subject 3 (out of 100): 95
Enter attendance percentage: 90
Enter annual family income (Rs.): 200000

Enter details of student 2
Enter student name: Priya
Enter marks in Subject 1 (out of 100): 88
Enter marks in Subject 2 (out of 100): 92
Enter marks in Subject 3 (out of 100): 90
Enter attendance percentage: 95
Enter annual family income (Rs.): 220000

Enter details of student 3
Enter student name: Ravi
Enter marks in Subject 1 (out of 100): 80
Enter marks in Subject 2 (out of 100): 70
Enter marks in Subject 3 (out of 100): 75
Enter attendance percentage: 80
Enter annual family income (Rs.): 250000

Enter details of student 4
Enter student name: Anu
Enter marks in Subject 1 (out of 100): 90
Enter marks in Subject 2 (out of 100): 55
Enter marks in Subject 3 (out of 100): 85
Enter attendance percentage: 90
Enter annual family income (Rs.): 150000
```

## 5. Sample Output

```
--- STUDENT ELIGIBILITY RESULTS ---
Rahul: Eligible (Aggregate: 90.00%)
Priya: Eligible (Aggregate: 90.00%)
Ravi: Eligible (Aggregate: 75.00%)
Anu: Not Eligible (Aggregate: 76.67%)

--- SCHOLARSHIP MERIT LIST ---
1. Priya | Aggregate: 90.00% | Attendance: 95.0% | Income: Rs. 220000
2. Rahul | Aggregate: 90.00% | Attendance: 90.0% | Income: Rs. 200000
3. Ravi | Aggregate: 75.00% | Attendance: 80.0% | Income: Rs. 250000
```
