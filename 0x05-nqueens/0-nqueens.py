#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys

def is_safe(board, row, col):
    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the lower diagonal on the left
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(row):
        if row == N:
            solutions.append([[i, row] for i, row in enumerate(board)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
