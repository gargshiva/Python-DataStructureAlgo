# Worst case : O(n*n)
# Best case : O(n) -> Array is already sorted
def bubbleSort(arr):
    for i in range(len(arr)):
        is_swapped = False
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                is_swapped = True
                swap(arr, j - 1, j)
        if not is_swapped:
            break


def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


arr = [1, 2, 3]
bubbleSort(arr)
print(arr)
