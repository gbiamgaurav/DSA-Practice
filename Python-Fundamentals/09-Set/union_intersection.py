
# Set Union - Everything in Both sets
a = {10, 20, 30}
b = {10, 100, 200}

u = a.union(b)
print(u)


# Intersection - Common item in both sets
a = {10, 20, 30}
b = {10, 100, 200}

i = a.intersection(b)
print(i)



a = {10, 20, 100, 50}
b = {10, 20, 30}
c = a.union(b)
print(len(c))


a = {'a', 'e', 'x', 'y', 'i', 'f', 'k', 'c'}

all_vowels = {'a', 'e', 'i', 'o', 'u'}

present_vowels = all_vowels.intersection(a)
print(present_vowels)