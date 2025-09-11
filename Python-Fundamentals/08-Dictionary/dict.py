
data = {"Name": "C Programming", "Pages": 250, "Price": 1000, "Ratings": 5}
print(data)


# Access the items
data["Name"]

data.get("Pages")

data["Ratings"]


var = "Pages"

if var in data:
    print("Yes")
else:
    print("No")


var = "Price"

if var in data:
    print(data[var])
else:
    print("Key not found")


my_dict = {"Apple": 250, "Orange": 300, "Mango": 50}

print(my_dict["Apple"])

