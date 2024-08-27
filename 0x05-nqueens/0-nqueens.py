#!/usr/bin/env python3
import sys

def print_solutions(solutions):
    """Print the solutions in the required format."""
    for solution in solutions:
        print(solution)

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """Solve the N-Queens problem and return all solutions."""
    def backtrack(row=0):
        if row == N:
            solution = [[i, board[i]] for i in range(N)]
            solutions.append(solution)
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * N
    solutions = []
    backtrack()
    return solutions
