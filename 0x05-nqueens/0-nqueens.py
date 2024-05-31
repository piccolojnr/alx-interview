#!/usr/bin/env python3
"""
N-Queens Problem
The N Queens problem is the problem of placing N chess queens on
an N×N chessboard so that no two queens attack each other.
This program solves the N Queens problem using backtracking.
The program takes an integer N from the command line and
prints all possible solutions to the problem.
The program assumes that N is at least 4.
Usage:
$ python3 nqueens.py N
"""
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """Solve the N Queens problem using backtracking"""
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_nqueens_util(board, col + 1):
                return True

            board[i][col] = 0

    return False


def solve_nqueens(N):
    """Solve the N Queens problem and print all solutions"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(col):
        if col >= N:
            sl = [[i, row.index(1)] for i, row in enumerate(board)]
            solutions.append(sl)
            return

        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
