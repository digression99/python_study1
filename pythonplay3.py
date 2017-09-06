# dictionary test

# dict = {}
# dict['one'] = "hey, this is one"
# dict[2] = "hey, this is two"
#
# tinydict = {'name' : 'john', 'code' : 1111, 'dept' : 'sales'}
#
# print(dict['one'])
# print(dict[2])
#
# print(tinydict.keys())
# print(tinydict.values())

# tuple test

import numpy as np
# a = np.array([1, 2, 3])
#
# print(type(a))
# print(a.shape)
# print(a[0], a[1], a[2])
# a[0] = 5
# print(a)
#
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print("b is ")
# print(b)
# print(b.shape)
# print(b[0, 0], b[1, 1], b[1, 0])
#
# c = np.zeros((2, 2))
# #print(c)
#
# d = np.ones((4, 4))
# #print(d)
#
# e = np.ones((4, 4))
#
# f = d * e
# print("f is")
# print(f)
#
# g = np.eye(4)
# print(g)

test1 = np.array([[1, 2], [3, 4]])
test2 = np.array([[5, 6], [7, 8]])
test3 = np.multiply(test1, test2)
test4 = np.dot(test1, test2)

#print(test3)
#print(test4)

cc = np.full((2, 2), 7)
#print(cc)

rd = np.random.random((2, 2))
scale = np.full((2, 2), 100)

rd = np.multiply(rd, scale)
rd = np.floor(rd)

#print(rd)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#print(a)

b = np.array([0, 2, 0, 1])
#print(a[np.arange(4), b]) #IndexError: index 3 is out of bounds for axis 0 with size 3

a = np.array([[1, 2], [3, 4], [5, 6]])
boolIdx = (a > 2)

#print(boolIdx)
#print(a[boolIdx])

x = np.array([[1, 2], [3, 4]])
x = x.T

#print(x)

v = np.array([1, 2, 3])
v = v.T
#print(v)

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
v = np.array([1, 0, 1, 0])
#y = np.empty_like(x)

# for i in range(3):
#     y[i, :] = x[i, :] + v

#print("y : ", y)

# vv = np.tile(v, (3, 1))
#
# print(vv)
#
# y = x + vv
# print(y)

y = x + v
print(y)