"""Real-world applications
The N-Queens problem has real-world applications such as: 
Task scheduling and assignment 
Computer resource management 
VLSI testing 
Traffic control 
Constraint satisfaction problem 
Load balancing in a multiprocessor computer"""
# 6. Backtracking Algorithms

# N-Queens Problem
"""Application: Backtracking is widely used for solving constraint satisfaction problems, puzzles, and combinatorial optimization problems.
Example: Used in solving puzzles like Sudoku or crosswords, and in AI applications where feasible solutions are constructed incrementally, like in game development or scheduling tasks."""


def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0
        return False

    board = [[0] * n for _ in range(n)]
    if solve(board, 0):
        return board
    else:
        return None
    
# Test N-Queens (for a 4x4 board)
solution_queens = solve_n_queens(4)
print("4-Queens Solution:")
for row in solution_queens:
    print(row)  
# Expected: A valid solution like:
# [0, 1, 0, 0]
# [0, 0, 0, 1]
# [1, 0, 0, 0]
# [0, 0, 1, 0]
    