# Given a bag  with capacity c and items with weight and value. Write a algorithm to find the max value


# Brute Force approach
# Either you can pick the item or drop the item
# Max(include_item , exclude_item)
# Greedy approach : Try out all the options
# Divide and conquer
def max_profit_brute_force(index, capacity, weight, value, total_item):
    if capacity <= 0:
        return 0

    if index == total_item:
        return 0

    if weight[index] <= capacity:
        include_item_profit = value[index] + max_profit_brute_force(index + 1, capacity - weight[index],
                                                                    weight,
                                                                    value, total_item)
        exclude_item_profit = max_profit_brute_force(index + 1, capacity, weight, value, total_item)
        return max(include_item_profit, exclude_item_profit)

    else:
        exclude_item_profit = max_profit_brute_force(index + 1, capacity, weight, value, total_item)
        return exclude_item_profit


total_items = 5
weights = [2, 4, 3, 5, 5]
values = [3, 4, 1, 2, 6]
bag_capacity = 11

cache = [[-1] * int(bag_capacity + 1) for _ in range(total_items + 1)]


# Start with bigger problem and come down to smaller problem
def max_profit_top_down_approach(index, capacity, weight, value, items):
    if capacity <= 0:
        return 0
    if index == items:
        return 0

    if cache[index][capacity] != -1:
        return cache[index][capacity]

    if weight[index] <= capacity:
        include_item_profit = value[index] + max_profit_top_down_approach(index + 1, capacity - weight[index], weight,
                                                                          value, items)
        exclude_item_profit = max_profit_top_down_approach(index + 1, capacity, weight, value, items)
        cache[index][capacity] = max(include_item_profit, exclude_item_profit)
        return cache[index][capacity]
    else:
        exclude_item_profit = max_profit_top_down_approach(index + 1, capacity, weight, value, items)
        cache[index][capacity] = exclude_item_profit
        return cache[index][capacity]


print("Max Profit : {}".format(max_profit_top_down_approach(0, bag_capacity, weights, values, total_items)))


# Start with smaller problem then go up to solve bigger problem
def max_profit_bottom_up_approach(index, capacity, weight, value, items):
    pass
