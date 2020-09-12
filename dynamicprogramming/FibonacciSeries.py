# Find nth number in Fibonacci Series

cache = [None] * 100


# Brute force
# Time Complexity : O (2n)
# Space Complexity : O(1)
def fibonacci_number_brute_force(n):
    if n <= 1:
        return n
    print("calling {}".format(n))
    return fibonacci_number_brute_force(n - 1) + fibonacci_number_brute_force(n - 1)


print("Fibonacci Number : {} ".format(fibonacci_number_brute_force(16)))


# Start with bigger problem , come down to smaller problem
# Divide and conquer technique
# DP - Top down approach
# Time Complexity : O(N) , Since we are calculating sub-problem only once
# Space Complexity : O(N) , To save the results of sub-problem
def fibonacci_number_bottom_up_approach(n):
    if cache[n] is not None:
        return cache[n]

    if n <= 1:
        return n

    cache[n] = fibonacci_number_bottom_up_approach(n - 1) + fibonacci_number_bottom_up_approach(n - 2)
    return cache[n]


print("Fibonacci Number : {} ".format(fibonacci_number_bottom_up_approach(32)))


# Start with smaller problem and then go to bigger problem
# Store the results of smaller problem
# DP - Bottom up approach
# Time Complexity : O(N) , Since we are calculating sub-problem only once
# Space Complexity : O(N) , To save the results of sub-problem
# Can we further optimise the Space complexity ?
def fibonacci_number_top_down_approach(n):
    table = [None] * 100
    table[0] = 1
    table[1] = 1
    for i in range(2, n):
        table[i] = table[i - 1] + table[i - 2]

    return table[n - 1]


print("Fibonacci Number : {} ".format(fibonacci_number_top_down_approach(32)))
