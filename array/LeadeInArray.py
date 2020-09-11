import sys


def find_leader(arr):
    print("Input Array {}".format(arr))
    max_till_now = - sys.maxsize
    for i in reversed(range(0, len(arr))):
        if arr[i] > max_till_now:
            print("Leader : {}".format(arr[i]))
            max_till_now = arr[i]


arr = [15, 16, 3, 2, 6, 1, 4]
find_leader(arr)
