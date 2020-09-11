def merge_sorted_arrays(arr1, arr2):
    print(arr1)
    print(arr2)
    ptr1 = 0
    ptr2 = 0
    op = []
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            op.append(arr1[ptr1])
            ptr1 += 1
        elif arr2[ptr2] < arr1[ptr1]:
            op.append(arr2[ptr2])
            ptr2 += 1
        else:
            op.append(arr1[ptr1])
            op.append(arr2[ptr2])
            ptr1 += 1
            ptr2 += 1

    while ptr2 < len(arr2):
        op.append(arr2[ptr2])
        ptr2 += 1

    while ptr1 < len(arr1):
        op.append(arr1[ptr1])
        ptr1 += 1

    return op


arr1 = [1, 3, 4, 10]
arr2 = [2, 4, 6]

merged_array = merge_sorted_arrays(arr1, arr2)
print(merged_array)
