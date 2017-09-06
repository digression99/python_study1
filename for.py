st = 10
fin = 20
step = int(input('enter the step : '))

for i in range(st, fin, step):
    print(i)
else:
    print('done')

for i in range(fin, st):
    print(i)
else:
    print('done')