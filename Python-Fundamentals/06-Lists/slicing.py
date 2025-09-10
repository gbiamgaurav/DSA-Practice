
numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])

print(numbers[-4:-1])

# Slicing with default values

print(numbers[:3])

print(numbers[3:])

# Assigment in lists

numbers = [10, 20, 30, 40, 50]
numbers[0:3] = [-1, -2, -3]

print(numbers)

# Remove elements from a list

numbers = [10, 20, 30, 40, 50]

numbers[1:3] = []

print(numbers)


# Copy of the list

numbers = [10, 20, 30, 40, 50]

num_copy = numbers[:]
print(num_copy)

numbers[2] = 100

print(num_copy)
print(numbers)


# Remove the list

numbers = [10, 20, 30, 40, 50]

num_remove = numbers[:] = [] 

print(num_remove)


numbers = [10, 20, 30, 40, 50, 60, 70]

numbers[:3] = []
print(numbers)

numbers[:3]

numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[2:5])