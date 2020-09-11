cache = [None] * 100


def print_fibonacci_series(n):
    series = []
    for i in range(1, n + 1):
        num = fibonacci_num(i)
        series.append(num)

    return series


def fibonacci_num(n):
    if n <= 2:
        return 1

    if cache[n] is not None:
        print("Cache Hit for {}".format(n))
        return cache[n]

    num = fibonacci_num(n - 1) + fibonacci_num(n - 2)
    cache[n] = num
    return num


# 1 1 2 3 5
print("Fibonacci Series : {}".format(print_fibonacci_series(10)))
