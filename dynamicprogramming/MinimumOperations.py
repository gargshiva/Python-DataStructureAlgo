'''
 Minimum operations to reach end of the array.
 At given index , you can make  steps from 0 to arr[index]
'''

import sys

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
cache = [-1 for i in range(0, len(arr) + 1)]


def minimum_steps_top_down(index, arr):
    if index == len(arr) - 1:
        return 0

    if index >= len(arr):
        return sys.maxsize

    if cache[index] != -1:
        return cache[index]

    steps = arr[index]
    min_steps = sys.maxsize
    for i in range(1, steps + 1):
        cache[index] = min(min_steps, 1 + minimum_steps_top_down(index + i, arr))
        min_steps = cache[index]

    return cache[index]


print("Min steps to reach end of array : {}".format(minimum_steps_top_down(0, arr)))
