def segregate(arr):
    print("Input array : {}".format(arr))
    ptr1 = 0
    ptr2 = len(arr) - 1
    while ptr1 < ptr2:
        if arr[ptr1] == 0:
            ptr1 = ptr1 + 1
        elif arr[ptr2] == 1:
            ptr2 = ptr2 - 1
        else:
            swap(arr, ptr1, ptr2)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = [0, 1, 0, 1, 0, 1, 0, 1, 0]
segregate(arr)
print("Output array : {}".format(arr))
