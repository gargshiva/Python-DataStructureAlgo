print([1, 2, "3", 4] == [2, "3", 4, 1])

numbers = [3, 1, 5, 2, 6, 2, 4, 5]
print(numbers[0])
print(numbers[-8])

print(numbers[2:5])
print(numbers[-5:-2])

print(numbers[:4])

print(numbers[4:])

print([1, 2] + [3, 5])

print(numbers[0: 6: 2])

# Reverse List
print(numbers[::-1])

# Memory location
print(numbers[:] is numbers)
name = "shiva"
print(name[:] is name)

# Search in List
print(3 in numbers)
print(3 not in numbers)

# Concat + Replication
