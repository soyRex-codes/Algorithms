# 4. Dynamic Programming Algorithms

# Knapsack Problem
"""Application: The Knapsack problem models resource allocation in many optimization problems.
Example: It's used in real-world decision-making, such as budgeting problems (allocating limited resources), cargo loading, portfolio management, and e-commerce for pricing and promotions."""

def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]


# Test Knapsack
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_value = knapsack(weights, values, capacity)
print("Knapsack (Max Value):", max_value)  # Expected: 7