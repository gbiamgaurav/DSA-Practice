
list = [10, 20, 30]

for x in list:
    print(x)
else:
    print("I will be executed")



a = 1 
while a <= 3:
    print(a)
    a += 1
else:
    print("I will be executed")



list = [10, 20, 30]

for x in list:
    print(x)
    if x == 20:
        break 
else:
    print("I will not be executed")



a = 1
while a <= 3:
    print(a)
    a += 1 
    if a == 2:
        break 
else:
    print("I will not be executed")



numbers = [2, 4, 6, 8]

for x in numbers:
    if x % 2 == 1:
        break
else:
    print("All are Even")