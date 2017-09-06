# 구구단 출력해보기



# for i in range (2, 10):
#     for j in range(1, 10):
#         print("{0} * {1} = {2}".format(i, j, i * j), end = ' ')
#     print(end = '\n')

# string 가지고 리스트 ?? 으로 리스트로 만든다.
# >>> user_input = input("Type your numbers\n")
# Type your numbers
# 1 2 3
# >>> [int(x) for x in user_input.split()]
# [1, 2, 3]


# test code

# str = input("enter 4 number : ")
# a = [int(x) for x in str.split()]
# print(a, type(a))

# for i in range(0, 4):
#     a.append(int(input()))
#a = list(input("numbers : {0}".format(b)))
    #a.append(int(input("lala : ")))
#
# a = [1, 2, 3, 4]
# b = [1, 2, 3, 4]
#
# if (a == b):
#     print("same")
# else:
#     print("dif")
#
# print(len(a))

import math

hw = "%s %s %d" % ("h", "w", 12)

print(hw)

xs = [3, 1, 'foo']
print(xs)

xs.pop()
print(xs)

animals = ['a', 'b', 'c']

for animal in animals:
    print(animal)

for idx, animal in enumerate(animals):
    print("#%d, %s" % (idx + 1, animal))

nums = [0, 1, 2, 3, 4]
nums2 = [x ** 2 for x in nums if x % 2 == 0]

print(nums2)

d = {'person': 2, 'cat': 4, 'spider': 8}

for animal in d:
    print('A %s has %d legs' % (animal, d[animal]))

for legs, animal in d.items():
    print(legs, animal)

dict2 = {x : x ** 2 for x in nums if x % 2 == 0}

print(dict2)

settest = {1, 2, 3}

settest2 = {math.sqrt(x) for x in settest}

print(settest2)

def printsign(x):
    if x > 0:
        return "pos"
    elif x < 0:
        return "neg"
    else:
        return "it's 0"

signlist = [-1, 0, 1]
for i in signlist:
    print(printsign(i))

class Greeter:
    def __init__(self, name = "bob"):
        self.name = name
    def greet(self, loud = False):
        if loud:
            print("hello, %s!" % self.name.upper())
        else:
            print("hello, %s!" % self.name)

g = Greeter('fred')
g.greet()
g.greet(loud = True)

