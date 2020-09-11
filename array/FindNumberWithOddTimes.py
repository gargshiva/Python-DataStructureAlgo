def find_number_with_odd_times(arr):
    print("Input Array : {}".format(arr))
    num = arr[0]
    for i in range(1, len(arr)):
        num = num ^ arr[i]

    return num


arr = [1, 1, 3, 2, 3]
print("Number with odd occurrence: {}".format(find_number_with_odd_times(arr)))
