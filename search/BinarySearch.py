# Assumption : Array is sorted
def binary_search(arr, item, start, end):
    mid = int((start + end) / 2)

    if start > end:
        return -1
    elif arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return binary_search(arr, item, start, mid - 1)
    else:
        return binary_search(arr, item, mid + 1, end)


arr = [1, 2, 3, 4, 5]
index = binary_search(arr, 5, 0, len(arr) - 1)
if index >= 0:
    print("Position : {}".format(index + 1))
else:
    print("Not found !")
