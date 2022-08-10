import random

print('Type max result for die you would like to roll')
print('Type exit to quit.')
sel = input()

while sel != 'exit':
    print('You rolled a ' + str(random.randint(1, int(sel))))
    print('Next roll:')
    sel = input()