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
