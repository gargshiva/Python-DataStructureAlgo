
# Assumption: At least 1 positive number in the array
# Kadane's Algorithm
def find_max_sum_subarr(arr):
    print("Input Array : {} ".format(arr))
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start_index = 0
    end_index = 0
    tmp = 0
    for i in range(1, len(arr)):
        if max_ending_here == 0:
            tmp = i

        max_ending_here = max_ending_here + arr[i]

        if max_ending_here < 0:
            max_ending_here = 0

        if max_ending_here > max_so_far:
            start_index = tmp
            end_index = i
            max_so_far = max_ending_here

    print("Start Index : {} ".format(start_index))
    print("End Index : {} ".format(end_index))
    print("Maximum Sum of subarray : {} ".format(max_so_far))


# Works even if all the numbers are negative
def find_max_sum_subarr_negative_numbers(arr):
    print(arr)


find_max_sum_subarr([4, -3, -2, 2, 3, 1, -2, -3, 4, 2, -6, -3, -1, 3, 1, 2])
