def left_array_rotation(arr, num):
    print("Input Array {}".format(arr))
    reverse(arr, 0, num - 1)
    reverse(arr, num, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)


def right_array_rotation(arr, num):
    print("Right - Input Array {}".format(arr))
    reverse(arr, len(arr) - num, len(arr) - 1)
    reverse(arr, 0, len(arr) - num - 1)
    reverse(arr, 0, len(arr) - 1)


def reverse(arr, i, j):
    while (i < j):
        swap(arr, i, j)
        i += 1
        j -= 1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr1 = [10, 20, 30, 40, 50]
left_array_rotation(arr1, 2)
print("Output Array {}".format(arr1))
