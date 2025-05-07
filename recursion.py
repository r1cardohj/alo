def count_down(i):
    print(i)
    # base case
    if i < 1:
        return
    # recursive case
    else:
        count_down(i-1)


count_down(3)
