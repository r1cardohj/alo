""" This is a recursive function same as for-loop"""

def sum(arr: list[int]):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])
