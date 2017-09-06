number = 23
running = True

while running == True:
    guess = int(input('enter any number : '))
    if guess == number:
        print('correct!')
        running = False
    elif guess < number:
        print('little more')
    else:
        print('little less')
else:
    print('the running loop is over')


print('done')
