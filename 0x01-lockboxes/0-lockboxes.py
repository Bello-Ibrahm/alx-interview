#!/usr/bin/python3
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

    The function uses a breadth-first search approach to explore the boxes
    starting from the first box (box 0).
    It uses a queue to process boxes and a set to track opened boxes.
    The function returns True if all boxes
    are opened, otherwise False.
    """
    # Number of boxes
    n = len(boxes)

    # A set to keep track of opened boxes
    opened_boxes = set()

    # A queue for breadth-first search (BFS)
    queue = []

    # Start the BFS from the first box (box 0)
    queue.append(0)
    opened_boxes.add(0)

    # Process the queue
    while queue:
        # Get the current box index from the front of the queue
        current_box = queue.pop(0)

        # Iterate through each key in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a box that has not yet been opened
            if key < n and key not in opened_boxes:
                # Add the box to the set of opened boxes
                opened_boxes.add(key)

                # Add the box index to the queue
                # for further processing
                queue.append(key)

    # Return True if all boxes are opened, otherwise False
    return len(opened_boxes) == n
