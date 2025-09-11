

# Modifying a value
data = {"Name": "C Programming", "Pages": 250, "Price": 1000, "Ratings": 5}

data["Price"] = 750

print(data)


# Add new value 
data["Author"] = "Log2Base2"
print(data)


# Remove an item
page_count = data.pop("Pages")
print(page_count)
print(data)


# Del method
del data["Price"]

print(data)


# Remove the entire dict
data.clear()

print(data)

del data

print(data)



fruits = {"apple": 250, "orange": 300, "mango":50}
#Write your code here

fruits["Apple"] = 500

fruits["Banana"] = 100

print(fruits)