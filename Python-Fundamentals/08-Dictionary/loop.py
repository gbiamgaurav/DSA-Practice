

data = {"Name": "C Programming", "Pages": 250, "Price": 1000, "Ratings": 5}

for x in data.keys():
    print(x)


for x in data.values():
    print(x)


for x, y in data.items():
    print(x, y)


for x, y in enumerate(data.items()):
    print(x, y)


