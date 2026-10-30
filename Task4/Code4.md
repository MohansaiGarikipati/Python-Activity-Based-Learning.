# Hackathon Team Formation and Ranking System – Python Project

## 1. Problem Statement

The Hackathon Team Formation and Ranking System is designed to organize students into teams and evaluate their performance in a hackathon. The system validates team sizes according to predefined minimum and maximum limits, records team members, and calculates total scores from multiple competition rounds.

## 2. Algorithm

1. Start the program.
2. Define the minimum and maximum team sizes.
3. Input the number of teams and the number of competition rounds.
4. For each team:
   - Enter the team name.
   - Enter the number of team members.
   - Validate the team size.
   - Enter the names and individual scores of all members.
   - Enter the team's score for each competition round.
5. Calculate the total team score by adding the round-wise scores.
6. Calculate the average individual student score.
7. Store the team details and calculated scores.
8. Sort teams using the following rules:
   - Total score in descending order.
   - Final-round score in descending order.
   - Average individual score in descending order.
   - Team name in alphabetical order.
9. Assign ranks to the teams.
10. Display team details, round-wise scores, total scores, and rankings.
11. Stop the program.

Assumptions for this project:

- Each team must contain 2 to 4 students.
- Each competition round is scored out of 100.
- Individual student scores are out of 100.
- The example uses three competition rounds.

## 3. Flowchart

START

Initialize team size limits and scoring rules

Input number of teams and competition rounds

Enter team name and member details

Is team size between 2 and 4?

No

Reject team details

Yes

Enter round-wise scores

Calculate total and average scores

Sort teams using tie-breaking rules

Display final rankings and team scores


## 4. Sample Input

The following example contains three teams and three competition rounds.

```
Enter number of teams: 3
Enter number of competition rounds: 3

Enter details for Team 1
Enter team name: Alpha
Enter number of team members: 2
Enter member 1 name: Ravi
Enter Ravi's individual score (0-100): 80
Enter member 2 name: Kiran
Enter Kiran's individual score (0-100): 90
Enter score for Round 1 (0-100): 80
Enter score for Round 2 (0-100): 80
Enter score for Round 3 (0-100): 90

Enter details for Team 2
Enter team name: Beta
Enter number of team members: 2
Enter member 1 name: Priya
Enter Priya's individual score (0-100): 90
Enter member 2 name: Sita
Enter Sita's individual score (0-100): 90
Enter score for Round 1 (0-100): 85
Enter score for Round 2 (0-100): 75
Enter score for Round 3 (0-100): 90

Enter details for Team 3
Enter team name: Gamma
Enter number of team members: 3
Enter member 1 name: Arjun
Enter Arjun's individual score (0-100): 70
Enter member 2 name: Arun
Enter Arun's individual score (0-100): 80
Enter member 3 name: Anil
Enter Anil's individual score (0-100): 90
Enter score for Round 1 (0-100): 80
Enter score for Round 2 (0-100): 80
Enter score for Round 3 (0-100): 80
```

## 5. Sample Output

```
--- HACKATHON TEAM RANKINGS ---

Rank: 1
Team Name: Beta
Members: Priya, Sita
Round Scores: [85.0, 75.0, 90.0]
Total Score: 250.00
Average Individual Score: 90.00

Rank: 2
Team Name: Alpha
Members: Ravi, Kiran
Round Scores: [80.0, 80.0, 90.0]
Total Score: 250.00
Average Individual Score: 85.00

Rank: 3
Team Name: Gamma
Members: Arjun, Arun, Anil
Round Scores: [80.0, 80.0, 80.0]
Total Score: 240.00
Average Individual Score: 80.00

The project helps organizers evaluate hackathon teams fairly and produce an organized ranking report.
