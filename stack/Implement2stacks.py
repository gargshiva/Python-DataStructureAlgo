# Implement 2 stacks with one array

class Stack:

    def __init__(self, size):
        self.arr = [None] * size
        self.ptr1 = -1
        self.ptr2 = size

    def push_stack1(self, element):
        if self.ptr1 + 1 == self.ptr2:
            raise Exception("Stack1 , Overflow")
        else:
            self.arr[self.ptr1 + 1] = element
            self.ptr1 += 1

    def pop_stack1(self):
        if self.ptr1 == -1:
            raise Exception("Stack1 , Underflow")
        else:
            self.ptr1 -= 1

    def push_stack2(self, element):
        if self.ptr2 - 1 == self.ptr1:
            raise Exception("Stack2 , Overflow")
        else:
            self.arr[self.ptr2 - 1] = element
            self.ptr2 -= 1

    def pop_stack2(self):
        if self.ptr2 == len(self.arr):
            raise Exception("Underflow")
        else:
            self.ptr2 += 1

    def print_stack1(self):
        for i in range(0, self.ptr1 + 1):
            print(self.arr[i], end=" ")

    def print_stack2(self):
        for i in reversed(range(self.ptr2, len(self.arr))):
            print(self.arr[i], end=" ")


stack = Stack(5)
stack.push_stack1(1)
stack.push_stack1(2)
# stack.push_stack1(3)
stack.print_stack1()
print()
stack.push_stack2(10)
stack.push_stack2(20)
stack.push_stack2(30)
stack.print_stack2()
