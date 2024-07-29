#!/usr/bin/python3
def canUnlockAll(boxes):
    opened = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in opened and key < len(boxes):
                opened.add(key)
                stack.append(key)

    return len(opened) == len(boxes)
