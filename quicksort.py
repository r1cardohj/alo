def quicksort(arr):
    """ 快排 """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []

        for i in arr[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)


        return quicksort(less) + [pivot, ] + quicksort(greater)


print(quicksort([1,4,2,2,5]))
