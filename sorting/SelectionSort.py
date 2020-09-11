def selection_sort(arr):
    print("Input Array : {}".format(arr))
    for i in range(len(arr)):
        min_index = find_min(arr, i)
        swap(arr, i, min_index)


def find_min(arr, i):
    min_index = i
    min = arr[i]
    for k in range(i + 1, len(arr)):
        if arr[k] < min:
            min = arr[k]
            min_index = k
    return min_index


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = [3, 1, 5, 2, 6, 3, -9]
selection_sort(arr)
print("Output Array : {}".format(arr))
