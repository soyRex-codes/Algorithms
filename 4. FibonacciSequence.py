# 4. Dynamic Programming Algorithms

# Fibonacci Sequence: Dynamic programming approach

"""Application: The Fibonacci sequence is useful in dynamic programming to optimize certain recursive problems.
Example: Used in memory caching or memoization problems, financial modeling (e.g., predicting stock behavior), and algorithm optimization problems in competitive programming."""

def fibonacci(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Test Fibonacci
fib_10 = fibonacci(10)
print("Fibonacci(10):", fib_10)  # Expected: 55
