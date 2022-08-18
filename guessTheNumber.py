#guess the number game
import random

print('Hello. Welcome to guess the number. What\'s your name?')
name = input()

print('Well ' + name + ', I\'m thinking of a number between 1 and 20.')
secretnumber = random.randint(1, 20)

for guessesTaken in range(1, 7): #loops 6 times then ends.
    print('Take a guess.')
    #print(secretnumber) #debug
    guess= int(input())
    
    if guess < secretnumber:
        print('Too low. Guess again.')
    elif guess > secretnumber:
        print('Too high. Guess again.')
    else:
        break #breaks when guessed correctly

if guess == secretnumber:
    print('Correct! the number is ' + str(secretnumber) + '!')
    print('You took ' + str(guessesTaken) + ' guesses.')
else:
    print('The number was ' + str(secretnumber) + '.')