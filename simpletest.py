#help(int)

def sumTotal(x, y):
    sum = 0
    for i in range(x, y):
        sum += i

    return sum

print('sumTotal(10, 20) = ', sumTotal(10, 20))

str = 'Rise to vote, sir.'
str = str.lower()

print(str)