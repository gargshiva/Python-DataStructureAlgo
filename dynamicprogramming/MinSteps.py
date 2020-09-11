# Minimum steps to reach end of array
import sys


def min_jumps(i, arr):
    if i == len(arr) - 1:
        return 0

    if i >= len(arr):
        return sys.maxsize

    steps = arr[i]
    min_value = sys.maxsize
    for j in range(1, steps + 1):
        min_value = min(min_value, min_jumps(i + j, arr))
    return min_value + 1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("Min Jumps : {}".format(min_jumps(0, arr)))
