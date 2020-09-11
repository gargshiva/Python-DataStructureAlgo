# Convert a array into zigzag array

def convert_zigzag_array(arr):
    print("Input Array : {}".format(arr))
    flag = 0
    for i in range(1, len(arr)):
        if flag == 0:
            if arr[i] < arr[i - 1]:
                swap(arr, i, i - 1)
            flag = 1
        else:
            if arr[i] > arr[i - 1]:
                swap(arr, i, i - 1)
            flag = 0


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = [3, 4, 6, 2, 1, 8, 9]
convert_zigzag_array(arr)
print("ZigZag Array : {}".format(arr))
