'''
Mad Libs Debug
Pawelski
3/21/2023
Python II
'''

repeat = "y"
while repeat == "y" or "yes" or "YES" or "Y":
    print("Mad Libs - Pizza")
print("Enter the indicated words to complete the story.")

# Input
adjective1 = input("Enter an adjective >> ")
nationality = input("Enter a nationality >> ")
person = input("Enter a person >> ")
noun1 = input("Enter a noun >> ")
adjective2 = input("Enter an adjective >> ")
noun2 = input("Enter a noun >> ")
adjective3 = input("Enter an adjective >> ")
adjective4 = input("Enter an adjective >> ")
plural_noun = input("Enter a plural noun >> ")
noun3 = input("Enter a noun >> ")
number1 = float(input("Enter a number >> "))
shape = input("Enter a shape >> ")
food1 = input("Enter a food >> ")
food2 = input("Enter a food >> ")
number2 = float(input("Enter a number >> "))

# Story
print()
print("Pizza was invented by a " + adjective1 + " "
      + nationality + " chef named " + person + ".")
print("To make a pizza, you need to take a lump of "
      + noun1 + ", and make a thin, round " + adjective2
      + " " + noun2 + ".")
print("Then you cover it with " + adjective3 + " sauce, "
      + adjective4 + " cheese, and fresh chopped "
      + plural_noun + ".")
print("Next you have to bake it in a very hot " + noun3 + ".")
print("When it is done, cut it into " + str(number1) + " "
      + shape + "s.")
print("Some kids like " + food1 + " pizza, but my favorite is the "
      + food2 + " pizza.")
print("If I could, I would eat pizza " + str(number2)
      + " times a day!")

input("Would you like to complete the Mad Libs again? (y/n) >> ")