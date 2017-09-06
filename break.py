while True:
    s = input('enter any string : ')
    if s == 'quit':
        break
    else:
        print('the length of the string is ', len(s))
else:
    print('done')

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    # Do other kinds of processing here...