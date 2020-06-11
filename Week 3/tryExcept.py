'''
try:
    userInput = int(input("Give me a number: "))
    print(userInput)
except:
    print("That is not a number!")
'''


inputList = []

while len(inputList)<10:
    try:
        userInput = int(input("Gib numbr - "))
        print("Nomnomnomnomnom")
        inputList.append(userInput)
    except:
        print("That not nbr")

print(inputList)