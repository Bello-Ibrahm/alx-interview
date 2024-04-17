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
    # Number of boxes
    n = len(boxes)

    # A set to keep track of opened boxes
    opened_boxes = set()

    # Recursive function to perform DFS and open boxes
    def dfs(current_box):
        # If the current box is already opened, return
        if current_box in opened_boxes:
            return

        # Mark the current box as opened
        opened_boxes.add(current_box)

        # Iterate through each key in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a valid box index,
            # recursively open the box
            if 0 <= key < n:
                dfs(key)

    # Start the DFS from the first box (box 0)
    dfs(0)

    # Return True if all boxes are opened, else return False
    return len(opened_boxes) == n
