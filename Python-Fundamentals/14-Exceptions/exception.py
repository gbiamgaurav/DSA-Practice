
# Handle Exception using Try Except

def div(a, b):
    try:
        print(a/b) 
    except:
        print("Something went wrong")


div(5, 2)

div(1, 0)

div(2, 1.2)


# Handle exception using Try, except and else

def div(a, b):
    try:
        print(a/b)
    except:
        print("Something went wrong")
    else:
        print("Division completed successfully")


div(10, 5)
div(10, 0)

# Handle exception using try, except, else, finally

def div(a, b):
    try:
        print(a/b)
    except:
        print("Something went wrong")
    finally:
        print("Division completed successfully")


div(10, 2)

div(10, 0)
