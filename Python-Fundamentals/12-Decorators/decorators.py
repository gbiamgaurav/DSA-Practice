
def first():
    print("Hello")


second = first()

second()


def add(n):
    return n + 10

def mul(n):
    return n * 10

def calculation(fun, val):
    print(fun(val))

calculation(add, 10)

calculation(mul, 10)


# Decorators 

def decorator(arg):

    def new_func():

        # Statements

        arg()

        # Statements

    return new_func


# example - use @

import time

# This is the decorator function
def timer_decorator(func):
    """A decorator that measures the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()
        print(f"'{func.__name__}' ran in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

# Use the decorator with the '@' symbol
@timer_decorator
def example_function(n):
    """A simple function that calculates the sum of numbers up to n."""
    total = sum(range(n + 1))
    return total

# Call the decorated function
example_function(10000000)