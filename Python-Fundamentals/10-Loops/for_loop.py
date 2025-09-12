
# Iterate String
for char in "Python":
    print(char)


# Iterate List
list = [10, 20, 30, 40]
for x in list:
    print(x)


vowels = "aeiou"

vowel_count = 0 

input_str = input("Enter an string here: ")

for char in input_str:
    if char in vowels:
        vowel_count += 1

print(vowel_count)