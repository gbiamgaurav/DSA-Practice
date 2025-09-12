
i = 1 
while i <= 3:
    print("Outer loop Iteration ", i)

    j = 1 
    while j <= 3:
        print("Inner loop Iteration ", j)

        j += 1

    i += 1 

    print("-------------------")

i = 1

while i <= 5:
    
    j = 1

    while j <= 5:
        print("*", end="")
        j += 1

    print()
    i += 1