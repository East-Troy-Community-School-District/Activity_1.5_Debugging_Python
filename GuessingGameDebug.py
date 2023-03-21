'''
Guessing Game Debug
Pawelski
3/21/2023
Python II
'''

import random

repeat = "n"
while repeat == "y":
    print("I am thinking of a number between 1 and 100...")
    mystery_num = randint(1, 100)
    guess = int(input("Guess my number >> "))
    guesses = 1
    while guess == mystery_num
        if guess > mystery_num:
            print("Too high!")
        elif guess < mystery_num;
            print("Too low!")
        guess = input("Guess my number >> ")
        guesses += guesses + 1
    print("You guessed my mystery number!")
    print("It took you", "guesses", "guesses to get", mystery_num)
    repeat = int(input("Would you like to play again (y/n) >> "))
    print()