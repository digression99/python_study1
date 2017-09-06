number = 23
guess = int(input('enter any number : '))

if guess == number:
    print('correct!')
elif guess < number:
    print('little more')
else:
    print('little less')

print('done')