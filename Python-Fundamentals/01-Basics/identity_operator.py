
x = 10 
y = 10

if x is y:
    print("x and y have the same identity")
else:
    print("x and y have different identity")

x = 10
y = 20 

if x is y:
    print("Same")
else:
    print("Different")


a = [1, 2, 3]
b = [1, 2, 3]

if a is not b:
    print("Different")
    print(id(a))
    print(id(b))
    
else:
    print("Same")
    