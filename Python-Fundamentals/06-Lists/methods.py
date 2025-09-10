
# Length of a list
numbers = [10, 20, 30, 40]

print(len(numbers))


# Concatenate 2 Lists
a = [10, 20, 30]
b = [40, 50]

c = a + b 
print(c)


# Append items 
numbers = [10, 20, 30, 40]
numbers.append(50)
print(numbers)


# Inserting items to a list
numbers = [10, 20, 30, 40, 50]

numbers.insert(2, 100)
print(numbers)

numbers.insert(0, 200)
print(numbers)


# Remove items from a list
numbers = [10, 20, 30, 40, 50]
numbers.remove(10)

print(numbers)

numbers.remove(50)
print(numbers)


del numbers[0]

print(numbers)
