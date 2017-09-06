shoplist = ['apple', 'mango', 'carrot', 'banana']

print('i have', len(shoplist), ' items to purchase.')

print('these items are', end=' ')
for item in shoplist:
    print(item, end=' ')

print('i also have to buy rice.')
shoplist.append('rice')
print('my shopping list is now ', shoplist)

print('i will sort my list now')
shoplist.sort()
print('sorted item list is,', shoplist)

print('the first item I have to buy is, ', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('i bought the old item,', olditem)
print('my shoplist is now, ', shoplist)
