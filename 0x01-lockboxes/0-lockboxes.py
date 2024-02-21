#!/usr/bin/python3


"""
LockBoxes
"""


def canUnlockAll(boxes):
    """Can unlock all
    """
    box_len = len(boxes)
    unlocked_ = [0]
    for id_, box in enumerate(boxes):
        if box:
            for x in box:
                if 0 <= x < box_len and x not in unlocked_ and x != id_:
                    unlocked_.append(x)
    return len(unlocked_) == len(boxes)
