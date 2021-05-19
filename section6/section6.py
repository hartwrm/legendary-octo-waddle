#Guess the number game

import random

print('whats ya name')
name = input()

print('hello ' + name, " I'm thinking of a number between 1 and 20")
secretNumber = random.randint(1, 20)

# print("DEBUG: the secret number is " + str(secretNumber))

for guessTaken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('too low')
    elif guess > secretNumber:
        print("too high")
    else:
        break #guessed the number 

if guess == secretNumber:
    print("good job, you took " + str(guessTaken) + " guesses")
else:
    print("nope, the number i was thinking of was " + str(secretNumber))