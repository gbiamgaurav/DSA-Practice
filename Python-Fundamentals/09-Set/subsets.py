
# Subsets
a = {10, 20, 30}
b = {10, 20, 30, 40, 50, 60, 70}

print(a.issubset(b))
print(b.issubset(a))


# Supersets
b = {10, 20, 30, 40, 50, 60, 70}
a = {10, 20, 30}

print(a.issuperset(b))
print(b.issuperset(a))


# Disjoint Set
a = {10, 20, 30}
b = {10, 100, 200}

print(a.isdisjoint(b))
print(b.isdisjoint(a))


a = {10, 20, 30}
b = {500, 100, 200}

print(a.isdisjoint(b))
print(b.isdisjoint(a))



a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {2, 4, 6, 8}

print(a.issuperset(b))
print(b.issuperset(a))