def reverse(arr):
    print("Input Array : {} ".format(arr))
    ptr1 = 0
    ptr2 = len(arr) - 1
    while ptr1 < ptr2:
        swap(arr, ptr1, ptr2)
        ptr1 += 1
        ptr2 -= 1


def swap(arr, ptr1, ptr2):
    temp = arr[ptr1]
    arr[ptr1] = arr[ptr2]
    arr[ptr2] = temp


arr = [1, 2, 3, 4, 5, 6]
reverse(arr)
print("Output Array : {} ".format(arr))
