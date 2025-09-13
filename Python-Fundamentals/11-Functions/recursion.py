
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


factorial(4)


n = int(input("Enter a number: "))

if n >= 0:
    ans = factorial(n)
    print(ans)



def display(num):
    if num == 0:
        return 
    display(num-1)
    print(num)

display(5)