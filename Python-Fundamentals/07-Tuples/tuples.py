
data = (10, 20, 30)

print(data)

# Access tuple items

print(data[0])
print(data[2])


if 10 in data:
    print("Yes")
else:
    print("No")


if 50 in data:
    print("Yes")
else:
    print("No")


data = (10, "abc", 3.15)

if 3.15 in data:
    print("Yes")
else:
    print("No")