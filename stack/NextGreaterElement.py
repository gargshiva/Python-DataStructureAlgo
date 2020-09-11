def find_next_greater_element(arr):
    print("Input Array : {}".format(arr))
    stack = []
    for i in arr:
        while len(stack) > 0 and stack[len(stack) - 1] < i:
            print("Next Greater element for {} is {} ".format(stack.pop(), i))
        stack.append(i)

    while len(stack) != 0:
        print("Next Greater element for {} Doesn't exist ".format(stack.pop()))


arr = [1, 2, 3, 4, 5]
find_next_greater_element(arr)