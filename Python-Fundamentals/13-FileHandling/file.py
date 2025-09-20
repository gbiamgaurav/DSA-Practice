
import os 

# One line at a time
f = open("file.txt", "r") 
print(f.readline())


# Multiple lines at a time
f = open("file.txt", "r")
for x in f:
    print(x, end=" ")


# Multiple lines as a list
f = open("file.txt", "r")
list = f.readlines()
print(list)


# Close the file
f.close()