def find_smallest(arr):
    smallest = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            idx = i

    return idx


def selection_sort(arr):
    res = []
    copy = list(arr)
    for _ in range(len(copy)):
        smallest_idx = find_smallest(copy)
        res.append(copy.pop(smallest_idx))
    return res


print(selection_sort([5, 3, 6, 2, 10]))
