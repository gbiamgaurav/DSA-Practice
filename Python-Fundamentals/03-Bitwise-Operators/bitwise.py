print("Welcome to the Bitwise Operators Demo!")
a = 15  # 1111 in binary
b = 4   # 0100 in binary

# Bitwise AND
bitwise_and = a & b
print(f"Bitwise AND: {a} & {b} = {bitwise_and}")

# Bitwise OR
bitwise_or = a | b
print(f"Bitwise OR: {a} | {b} = {bitwise_or}")

# Bitwise XOR
bitwise_xor = a ^ b
print(f"Bitwise XOR: {a} ^ {b} = {bitwise_xor}")

# Bitwise NOT
bitwise_not = ~a
print(f"Bitwise NOT: ~{a} = {bitwise_not}")

# Left Shift
left_shift = a << 2
print(f"Left Shift: {a} << 2 = {left_shift}")

# Right Shift
right_shift = a >> 2
print(f"Right Shift: {a} >> 2 = {right_shift}")

print("Thank you for using the Bitwise Operators Demo!")