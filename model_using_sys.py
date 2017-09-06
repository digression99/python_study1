import sys
import os

print('the command line arguments are :')
for i in sys.argv:
    print(i)

print('\n\nthe python path is ', sys.path, '\n')

print(os.getcwd())