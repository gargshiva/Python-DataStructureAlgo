# Search an element in sorted and rotated array

def find_element(arr, element):
    end = len(arr) - 1
    pivot_index = find_pivot_index(arr, 0, len(arr) - 1)
    print("Pivot Index : {} ".format(pivot_index))
    if arr[pivot_index] == element:
        return pivot_index
    elif arr[pivot_index + 1] <= element <= arr[end]:
        return binary_search(arr, pivot_index + 1, end, element)
    elif arr[0] <= element <= arr[pivot_index - 1]:
        return binary_search(arr, 0, pivot_index - 1, element)
    else:
        return -1


def binary_search(arr, start, end, element):
    mid = int((start + end) / 2)
    if start > end:
        return -1
    elif arr[mid] == element:
        return mid
    elif arr[mid] > element:
        return binary_search(arr, start, mid - 1, element)
    else:
        return binary_search(arr, mid + 1, end, element)


def find_pivot_index(arr, start, end):
    mid = int((start + end) / 2)
    if start > end:
        return -1
    elif arr[mid - 1] > arr[mid] < arr[mid + 1]:
        return mid
    elif arr[mid] < arr[end]:
        return find_pivot_index(arr, start, mid - 1)
    else:
        return find_pivot_index(arr, mid + 1, end)


arr = [4, 5, 1, 2, 3]
print("Element found at Index :  {}".format(find_element(arr, 3)))

arr = [3, 4, 5, 1, 2]
print("Element found at Index :  {}".format(find_element(arr, 3)))
