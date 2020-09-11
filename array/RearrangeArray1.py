# Rearrange array in such that arr[j] becomes 'i' if arr[i] is 'j'

def rearrange_array_1(arr):
    temp = [None] * len(arr)
    for i in range(0, len(arr)):
        j = arr[i]
        temp[j] = i

    for k in range(0, len(temp)):
        arr[k] = temp[k]


arr = [1, 4, 0, 3, 2]
rearrange_array_1(arr)
print(arr)
