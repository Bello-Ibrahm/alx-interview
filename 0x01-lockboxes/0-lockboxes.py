#!/usr/bin/python
""" Lockboxes interview challenge """


def canUnlockAll(boxes):
    """
    Determines whether all boxes in a given list of boxes can be unlocked
    starting from the first box (box 0).

    Parameters:
    boxes (list of list of int): A list of lists, where each sublist
    represents a box that contains keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, otherwise False.

    The function follows a breadth-first search approach using a queue
    to keep track of the boxes that have been unlocked.
    Initially, the function starts with the first box (box 0),
    which is considered unlocked. The function then processes the
    queue, iterating through each key in the current box and unlocking
    the corresponding box if it has not been opened yet. It continues
    until there are no more boxes left to process in the queue.

    If all boxes are opened (i.e., the length of the set of opened boxes
    is equal to the total number of boxes), the function
    returns True. Otherwise, it returns False.
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
