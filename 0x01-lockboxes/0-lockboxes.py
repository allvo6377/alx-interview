#!/usr/bin/python3
'''A module for working with lockboxes.
'''
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Determine if all boxes can be unlocked.

    This function takes a list of boxes, where each box contains
    zero or more keys to other boxes. The first box is initially
    unlocked. The function determines if it is possible to unlock
    all the boxes by using the keys found in the unlocked boxes.

    Args:
        boxes (List[List[int]]): A list of boxes, where each box
                                 is represented by a list of
                                 integers. Each integer represents
                                 a key to another box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    """
    if not isinstance(boxes, list):
        return False

    n = len(boxes)

    if n == 0:
        return True

    keys = [0]
    unlocked = [False] * n
    unlocked[0] = True

    for key in keys:
        if not isinstance(boxes[key], list):
            continue

        for new_key in boxes[key]:
            if not isinstance(new_key, int) or new_key < 0 or new_key >= n:
                continue

            if not unlocked[new_key]:
                keys.append(new_key)
                unlocked[new_key] = True

    return all(unlocked)
