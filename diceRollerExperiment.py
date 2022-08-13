import random

""" print('Type max result for die you would like to roll')
print('Type exit to quit.')
sel = input()

while sel != 'exit':
    print('You rolled a ' + str(random.randint(1, int(sel))))
    print('Next roll:')
    sel = input() """

""" print('Type selection and press enter: D2  D4  D6  D8  D10  D12 D20  D100')
print('Type exit to quit.')
sel = input()

while sel != 'exit':
    roller = int(sel.lower().replace('d', ''))
    if roller == 2:
        print('Your result is ' + str(random.randint(1, roller)))
    elif roller == 4:
        print('Your result is ' + str(random.randint(1, roller)))
    elif roller == 6:
        print('Your result is ' + str(random.randint(1, roller)))
    elif roller == 8:
        print('Your result is ' + str(random.randint(1, roller)))
    elif roller == 10:
        print('Your result is ' + str(random.randint(1, roller)))
    elif roller == 12:
        print('Your result is ' + str(random.randint(1, roller)))
    elif roller == 20:
        print('Your result is ' + str(random.randint(1, roller)))
    elif roller == 100:
        print('Your result is ' + str(random.randint(1, roller)))
    else:
        print('Error: Invalid selection')
    print('Next selection?')
    sel = input() """

print('Type selection and press enter: D2  D4  D6  D8  D10  D12 D20  D100')
print('Type exit to quit.')
sel = input()

def roller(strip): #strip is the stripped integer input
    random.randint(1, strip)

while sel != 'exit':
    stripper = int(sel.lower().replace('d', ''))
    print('You rolled ' + str(roller(stripper)))
    print('Next selection:')
    sel = input()