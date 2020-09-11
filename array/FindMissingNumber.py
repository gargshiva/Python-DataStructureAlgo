def find_missing_number_sum_method(arr):
    print("{}".format(arr))
    input_size = len(arr) + 1
    expected_sum = (input_size * (input_size + 1)) / 2
    actual_sum = 0
    for i in arr:
        actual_sum = actual_sum + i
    return expected_sum - actual_sum


arr = [1, 2, 4, 5]
print("Missing Number = {}".format(int(find_missing_number_sum_method(arr))))
# print(15 ^ 12)
