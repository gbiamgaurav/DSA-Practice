
def display(day, month, year):
    print("Day :" + str(day))
    print("Month :" + str(month))
    print("Year :" + str(year))


def init():
    display(1, 4, 2025)


init()

# Default Arguments

def display(day, month, year=2025):
    print("Day: ", str(day))
    print("Month: ", str(month))
    print("Year: ", str(year))

display(1, 9)


# Keyword Arguments

def display(day, month, year):
    print("Day: ", str(day))
    print("Month: ", str(month))
    print("Year: ", str(year))

display(day=29, month=10, year=1988)
display(year=1988, day=29, month=10)


# Arbitary Arguments

# Actual Syntax
def func(*args):
    print(args)


def display(*data):
    print(data)

display("Alan", 25, 65.7)

def CheckSum(*nums):
    return sum(nums)


nums = [10, 20, 30, 40, 50, 60]

CheckSum(*nums)