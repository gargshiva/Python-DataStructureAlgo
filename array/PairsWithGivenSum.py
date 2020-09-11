def find_pairs_with_given_sum(arr, sum):
    print("Input Array : {}  , Input Sum : {}".format(arr, sum))
    arr.sort()
    ptr1 = 0
    ptr2 = len(arr) - 1
    while ptr1 < ptr2:
        s = arr[ptr1] + arr[ptr2]
        if s == sum:
            print("Pair({},{})".format(arr[ptr1], arr[ptr2]))
            ptr1 += 1
        elif s > sum:
            ptr2 -= 1
        else:
            ptr1 += 1


arr = [5, 8, 3, 4, 2, 6, 10, 7, 1, 9]
find_pairs_with_given_sum(arr, 11)
