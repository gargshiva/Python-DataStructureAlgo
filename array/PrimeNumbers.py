import math


def is_prime_number(num):
    print("Input number {}".format(num))
    if num == 1:
        return False
    if num == 2:
        return True

    res = True
    num_sqrt = math.ceil(math.sqrt(num))
    for i in range(3, num_sqrt):
        if num % i == 0:
            res = False
            break

    return res


print(is_prime_number(2))
