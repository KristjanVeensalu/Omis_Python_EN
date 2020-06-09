import random


'''
Write a program to guess a number between 1 to 9
User is prompted to guess the number, 
if they guess incorrectly, say wrong number
and ask for input again. If they do guess it, 
write Well guessed and exit the program.
'''

ourRandomNumber = random.randint(0,9)
ouruserInput = int(input("Guess a number> "))

if ourRandomNumber != ouruserInput:
    gameIsplaying = True
else:
    gameIsplaying = False
    print("Well guessed")


while gameIsplaying:
    if ourRandomNumber != ouruserInput:
        print("Wrong guess")
        ouruserInput = int(input("Guess again: "))
    if ourRandomNumber == ouruserInput:
        print("Well guessed")
        gameIsplaying = False

