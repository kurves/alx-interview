#!/usr/bin/python3
"""
This module defines a function to check if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    if not boxes:
        return False
    n = len(boxes)
    unlocked = [False] * n  # To keep track of unlocked boxes
    unlocked[0] = True  # The first box is always unlocked
    keys = [0]  # Start with the key for the first box

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key < n and not unlocked[new_key]:
                unlocked[new_key] = True
                keys.append(new_key)

    return all(unlocked)
