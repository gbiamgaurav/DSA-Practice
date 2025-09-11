

data = {10, 100, 200, 10}

# Modify set elements
data.add(500)
print(data)


data.update({1000, 250, 300})

print(data)


# Remove items from a set
data.remove(100)
print(data)


# Discard item
data.discard(500)
print(data)


# clear set
data.clear()
print(data)


# Delete set
del data

print(data)


data = {10, 20, 30}
#Write your code here

num = int(input("Enter the number here: "))

data.add(num)
print(data)
