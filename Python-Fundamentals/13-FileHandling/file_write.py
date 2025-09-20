

f = open("next.txt", "w")

f.write("Hello World\n")
f.close()


f = open("next.txt", "r")
print(f.read())
f.close()


# Append
f = open("next.txt", "a")
f.write("Welcome\n")
f.close()