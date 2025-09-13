
# Lambda expression
#lambda arguments: expression


val = lambda x, y: x + y

val(2, 5)


def fun(n):
    return lambda x: x ** n


square = fun(2)
square(2)

square(4)

cube = fun(3)
cube

cube(2)

cube(5)