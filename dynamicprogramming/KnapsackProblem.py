# Knapsack problem
# w = [2,4,3,5,5]
# v = [3,4,1,2,6]
# c = 5

def get_max_value(n, capacity, weight, value, index):
    if index == n or capacity <= 0:
        return 0

    if capacity >= weight[index]:
        vin = get_max_value(n, capacity - weight[index], weight, value, index + 1) + value[index]
        vex = get_max_value(n, capacity, weight, value, index + 1)
        return max(vin, vex)
    else:
        vex = get_max_value(n, capacity, weight, value, index + 1)
        return vex


weights = [2, 4, 3, 5, 5]
values = [3, 4, 1, 2, 6]
n = 5
capacity = 12

print("MaxValue : {}".format(get_max_value(n, capacity, weights, values, 0)))
