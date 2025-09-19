import os
import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

guess = int(guess)

if guess == number:
    print("You guessed it!")    
else:
    print("Wrong guess. The number was", number)