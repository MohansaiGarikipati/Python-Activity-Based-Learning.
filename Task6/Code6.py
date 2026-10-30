
# Multi-Branch Expense Matrix Analysis

branches = []
categories = []
expenses = []

try:
    n = int(input("Enter number of branches: "))
    m = int(input("Enter number of expense categories: "))

    if n <= 0 or m <= 0:
        print("Branches and categories must be positive.")

    else:
        # Input branch names
        for i in range(n):
            name = input(f"Enter branch {i + 1} name: ").strip()
            if not name:
                raise ValueError("Branch name cannot be empty.")
            branches.append(name)

        # Input expense category names
        for j in range(m):
            name = input(
                f"Enter expense category {j + 1}: "
            ).strip()

            if not name:
                raise ValueError("Category name cannot be empty.")

            categories.append(name)

        # Create expense matrix
        for i in range(n):
            print(f"\nEnter expenses for {branches[i]}")
            row = []

            for j in range(m):
                amount = float(
                    input(f"Enter {categories[j]} expense: Rs. ")
                )

                if amount < 0:
                    raise ValueError("Expense cannot be negative.")

                row.append(amount)

            expenses.append(row)

        # Calculate branch-wise totals and averages
        branch_totals = []
        branch_averages = []

        for row in expenses:
            total = sum(row)
            branch_totals.append(total)
            branch_averages.append(total / m)

        # Calculate category-wise totals and averages
        category_totals = []

        for j in range(m):
            total = sum(expenses[i][j] for i in range(n))
            category_totals.append(total)

        category_averages = [
            total / n for total in category_totals
        ]

        # Calculate overall expenditure
        overall_total = sum(branch_totals)

        # Identify largest contributors
        highest_branch = branch_totals.index(max(branch_totals))
        highest_category = category_totals.index(
            max(category_totals)
        )

        # Display expense matrix
        print("\n--- EXPENSE MATRIX ---")
        print("Branch", *categories, sep="\t")

        for i in range(n):
            print(branches[i], *expenses[i], sep="\t")

        # Display branch-wise analysis
        print("\n--- BRANCH-WISE ANALYSIS ---")

        for i in range(n):
            print(f"\nBranch: {branches[i]}")
            print(f"Total Expense: Rs. {branch_totals[i]:.2f}")
            print(
                f"Average Expense: Rs. {branch_averages[i]:.2f}"
            )

        # Display category-wise analysis
        print("\n--- CATEGORY-WISE ANALYSIS ---")

        for j in range(m):
            print(f"\nCategory: {categories[j]}")
            print(f"Total Expense: Rs. {category_totals[j]:.2f}")
            print(
                f"Average Expense: Rs. {category_averages[j]:.2f}"
            )

        # Display overall results
        print("\n--- OVERALL EXPENSE SUMMARY ---")
        print(f"Total Organizational Expense: Rs. {overall_total:.2f}")

        print(
            f"Highest Spending Branch: {branches[highest_branch]}"
        )
        print(
            f"Highest Spending Category: {categories[highest_category]}"
        )

except ValueError as e:
    print("Invalid input:", e)
