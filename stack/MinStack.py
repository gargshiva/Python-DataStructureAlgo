# Find minimum element in the stack in O(1)

stack = []
min_stack = []


class MinStack:

    def push_number(self, num):
        print("Push number {}".format(num))
        stack.append(num)
        if len(min_stack) == 0 or num < stack[len(min_stack) - 1]:
            min_stack.append(num)

    def pop_number(self):
        if len(stack) != 0:
            element = stack.pop(len(stack) - 1)
            print("Pop number from stack {} ".format(element))
            if element == min_stack[len(min_stack) - 1]:
                el = min_stack.pop(len(min_stack) - 1)
                print("Pop number from min stack {} ".format(el))

    def min_number(self):
        if len(stack) != 0:
            return min_stack[len(min_stack) - 1]


min_stack_obj = MinStack()
min_stack_obj.push_number(6)
min_stack_obj.push_number(7)
min_stack_obj.push_number(5)

print("Min Element {}".format(min_stack_obj.min_number()))

min_stack_obj.pop_number()

print("Min Element {}".format(min_stack_obj.min_number()))
