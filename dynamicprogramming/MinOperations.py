'''
 Given a starting number and end number.
 How many minimum operation required to reach from start to end number.
 Operations : Add 1 to number , Double the number

 Assumption : No operation is there to decrement
'''

import sys


def min_operations_brute_force(start, end):
    if start == end:
        return 0

    if start > end:
        return sys.maxsize

    addition = 1 + min_operations_brute_force(start + 1, end)

    start_after_mult_ops = start * 2

    if start_after_mult_ops != start:
        multiplication = 1 + min_operations_brute_force(start_after_mult_ops, end)
    else:
        multiplication = sys.maxsize

    return min(addition, multiplication)


print("Minimum operations : {}".format(min_operations_brute_force(0, 8)))

end = 8

cache = [[-1] * int(end + 1) for _ in range(end + 1)]


# Greedy approach
# Divide and Conquer
# DP - TopDown approach
def min_operations(start, end):
    if start == end:
        cache[start][end] = 10
        return 0

    if start > end:
        return sys.maxsize

    if cache[start][end] != -1:
        return cache[start][end]

    addition = 1 + min_operations(start + 1, end)

    start_after_mult_ops = start * 2

    if start_after_mult_ops != start:
        multiplication = 1 + min_operations(start_after_mult_ops, end)
    else:
        multiplication = sys.maxsize

    cache[start][end] = min(addition, multiplication)
    return cache[start][end]


print("Minimum operations : {}".format(min_operations(0, 8)))
