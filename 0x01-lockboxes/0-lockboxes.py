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
    if not boxes:
        return False

    current_keys: list = boxes[0]
    unlocked_boxes = []
    unlocked_boxes.append(0)

    while len(unlocked_boxes) != len(boxes) and len(current_keys) > 0:
        key = current_keys.pop(0)

        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.append(key)
            current_keys.extend(boxes[key])

    return True if len(unlocked_boxes) == len(boxes) else False
