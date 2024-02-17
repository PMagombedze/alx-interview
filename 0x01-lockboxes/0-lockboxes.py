#!/usr/bin/python3


"""
LockBoxes
"""


def canUnlockAll(boxes):
    """Can unlock all
    """
    unlockedBoxes = set([0])
    queue = [0]

    while queue:
        current = queue.pop(0)
        for keys in boxes[current]:
            if keys not in unlockedBoxes:
                unlockedBoxes.add(keys)
                queue.append(keys)
    return len(unlockedBoxes) == len(boxes)
