#!/usr/bin/python3
"""A function that determines if a box that contains a list
   of lists can be opened using keys stored inside the lists
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
