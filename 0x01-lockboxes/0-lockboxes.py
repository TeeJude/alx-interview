#!/usr/bin/python3
""" A function that determines if boxes can be opened.
"""

def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    spot = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or spot == 0:
            unlocked[spot] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != spot:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        spot += 1
    return False
