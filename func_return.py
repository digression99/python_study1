def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))

def returnInputs():
    x = int(input('enter number : '))

    if (x < 10):
        return x
    else:
        return None

print(returnInputs())

#pass??

def some_function():
    pass

