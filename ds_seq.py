shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])
# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3]) # only 1, 2
print('Item 2 to end is', shoplist[2:]) # only 2, 3
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
# 미쳤다. 이런 미친. 부분을 그냥 자유롭게 쓴다니, 포인터의 혁명이다.

#use step

print('step 1', shoplist[::1])
print('step 2', shoplist[::2])
print('step 3', shoplist[::3])
print('step -1?', shoplist[::-1])
