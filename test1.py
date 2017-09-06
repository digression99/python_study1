import math
import random
#
# n = float(input())
#
# print("cos : ", math.cos(n))
# print("sin : ", math.sin(n))
# print("tan : ", math.tan(n))

#n = int(input())

print("using list")
l = [random.sample(range(20), 10) for i in range(10)]
iter = iter(l)

print("using it")
for iter in l:
    print(iter)

#
# if n == 1:
#     #do something
# elif n == 2:
#     #do 2
# else:
    #do 3

