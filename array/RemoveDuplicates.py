# Remove duplicates from sorted array


class Solution:
    def __init__(self, inp):
        self.inp = inp

    def remove_duplicates_extra_space(self):
        print("Input Array : {}".format(self.inp))
        ptr1 = 0
        ptr2 = 1
        op = []
        while ptr1 < ptr2 < len(self.inp):
            if self.inp[ptr1] != self.inp[ptr2]:
                op.append(self.inp[ptr1])

            ptr1 = ptr1 + 1
            ptr2 = ptr2 + 1

        op.append(self.inp[ptr1])
        return op

    def remove_duplicates_in_place(self):
        j = 0
        for i in range(1, len(self.inp)):
            if self.inp[i - 1] != self.inp[i]:
                self.inp[j] = self.inp[i - 1]
                j = j + 1

        self.inp[j] = self.inp[i - 1]
        for k in range(0, j + 1):
            print(self.inp[k], end=' ')


obj = Solution([1, 1, 2, 3, 4, 4, 5, 5])
print(obj.remove_duplicates_extra_space())
obj.remove_duplicates_in_place()
