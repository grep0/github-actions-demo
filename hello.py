def add(x, y):
    """This is an add function"""

    return x + y

def multiply(x, y):
    if x==0:
        return x
    else:
        return add(multiply(x-1,y), y)


print(add(1, 1))
