# Dutch National Flag problem : Segregate numbers 0, 1, 2
def segregate_numbers(arr):
    m = 0
    j = len(arr) - 1
    i = 0
    while i <= j:
        if arr[i] == 0:
            swap(arr, i, m)
            i += 1
            m += 1
        elif arr[i] == 1:
            i += 1
        else:
            while arr[j] == 2:
                j = j - 1
            if i < j:
                swap(arr, i, j)


def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
segregate_numbers(arr)
print(arr)
