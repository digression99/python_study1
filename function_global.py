x = 50

def global_change():
    global x
    print('x is', x)
    x = 2
    print('changed x : ', x)

global_change()
print('done')

def say(message, times = 1):
    print(message * times)

say('hello')
say('world', 10)

def func(a, b=5, c=10):
    print('a is ', a, ' b is ', b, ' c is ', c)

#using keywords
func(c=20, a=10)

#function_varargs.py
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)
    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
        #tuple, dictionary의 개념을 잘 알자


print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))