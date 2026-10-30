
MIN_TEAM_SIZE = 2
MAX_TEAM_SIZE = 4
MAX_SCORE = 100

teams = []

try:
    n = int(input("Enter number of teams: "))
    rounds = int(input("Enter number of competition rounds: "))

    if n <= 0 or rounds <= 0:
        print("Number of teams and rounds must be positive.")

    else:
        for i in range(n):
            print(f"\nEnter details for Team {i + 1}")

            team_name = input("Enter team name: ").strip()

            if not team_name:
                print("Team name cannot be empty. Skipping team.")
                continue

            try:
                size = int(input("Enter number of team members: "))
            except ValueError:
                print("Invalid team size. Skipping team.")
                continue

            if not MIN_TEAM_SIZE <= size <= MAX_TEAM_SIZE:
                print("Invalid team size. Team must have 2 to 4 members.")
                continue

            members = []
            valid_team = True

            for j in range(size):
                name = input(f"Enter member {j + 1} name: ").strip()

                try:
                    score = float(
                        input(f"Enter {name}'s individual score (0-100): ")
                    )
                except ValueError:
                    print("Invalid individual score.")
                    valid_team = False
                    break

                if not name or not 0 <= score <= MAX_SCORE:
                    print("Invalid member name or score.")
                    valid_team = False
                    break

                members.append({
                    "name": name,
                    "score": score
                })

            if not valid_team:
                print("Team details rejected.")
                continue

            round_scores = []

            for r in range(rounds):
                try:
                    score = float(
                        input(f"Enter score for Round {r + 1} (0-100): ")
                    )
                except ValueError:
                    print("Invalid round score.")
                    valid_team = False
                    break

                if not 0 <= score <= MAX_SCORE:
                    print("Round score must be between 0 and 100.")
                    valid_team = False
                    break

                round_scores.append(score)

            if not valid_team:
                print("Team details rejected.")
                continue

            total = sum(round_scores)
            average_member_score = (
                sum(m["score"] for m in members) / len(members)
            )

            teams.append({
                "name": team_name,
                "members": members,
                "round_scores": round_scores,
                "total": total,
                "average_member_score": average_member_score
            })
        teams.sort(
            key=lambda t: (
                -t["total"],
                -t["round_scores"][-1],
                -t["average_member_score"],
                t["name"].lower()
            )
        )

        print("\n--- HACKATHON TEAM RANKINGS ---")

        if not teams:
            print("No valid teams available.")
        else:
            for rank, team in enumerate(teams, start=1):
                print(f"\nRank: {rank}")
                print(f"Team Name: {team['name']}")
                print("Members:", ", ".join(
                    m["name"] for m in team["members"]
                ))

                print("Round Scores:", team["round_scores"])
                print(f"Total Score: {team['total']:.2f}")
                print(
                    "Average Individual Score: "
                    f"{team['average_member_score']:.2f}"
                )

except ValueError:
    print("Please enter valid integers for teams and rounds.")

