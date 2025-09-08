## Syntax for nested if-elif-else statements in Python

"""if condition:
    #statement 

elif condition:
    #statement

elif condition:
    #statement

else:
    #statement"""


score = int(input("Enter your score: "))

if (score <= 100 and score >= 90):
    print("S")
elif (score < 90 and score >= 80):
    print("A")
elif (score < 80 and score >= 70):
    print("B")
elif (score < 70 and score >= 60):
    print("C")
elif (score < 60 and score >= 50):
    print("D")
elif (score < 50 and score >= 40):
    print("E")
elif (score < 40 and score >= 0):
    print("F")
else:
    print("Invalid Score")
