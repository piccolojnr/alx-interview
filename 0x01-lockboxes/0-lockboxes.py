#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes: list):
    """can unlock all lockboxes

    Args:
        boxes (list): is a list of lists

    Returns:
        _type_: boolean
    """
    keys: list = boxes[0]
    found = []
    found.append(0)

    while len(found) != len(boxes) and len(keys) > 0:
        key = keys.pop(0)

        if key < len(boxes) and key not in found:
            found.append(key)
            keys.extend(boxes[key])

    return True if len(found) == len(boxes) else False
