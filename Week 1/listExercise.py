'''Write a program that asks for use input (Only numbers),
adds that input to a list, then returns to the user>
the largest number in the list, the smallest number,
and the sum of the numbers. (The list is only 4 items long)
'''
firstValue = int(input("Enter a number> "))
secondValue = int(input("Enter a number> "))
thirdValue = int(input("Enter a number> "))
fourthValue = int(input("Enter a number> "))
containerList = [firstValue,secondValue,thirdValue,fourthValue]

if containerList[0]>containerList[1]:
    if containerList[0]>containerList[2]:
        if containerList[0]>containerList[3]:
                print("The largest value is: ", containerList[0])

if containerList[1]>containerList[0]:
    if containerList[1]>containerList[2]:
        if containerList[1]>containerList[3]:
                print("The largest value is: ", containerList[1])

if containerList[2]>containerList[0]:
    if containerList[2]>containerList[1]:
        if containerList[2]>containerList[3]:
                print("The largest value is: ", containerList[2])

if containerList[3]>containerList[0]:
    if containerList[3]>containerList[1]:
        if containerList[3]>containerList[2]:
                print("The largest value is: ", containerList[3])

if containerList[0]<containerList[1]:
    if containerList[0]<containerList[2]:
        if containerList[0]<containerList[3]:
                print("The smallest value is: ", containerList[0])

if containerList[1]<containerList[0]:
    if containerList[1]<containerList[2]:
        if containerList[1]<containerList[3]:
                print("The smallest value is: ", containerList[1])

if containerList[2]<containerList[0]:
    if containerList[2]<containerList[1]:
        if containerList[2]<containerList[3]:
                print("The smallest value is: ", containerList[2])

if containerList[3]<containerList[0]:
    if containerList[3]<containerList[1]:
        if containerList[3]<containerList[2]:
                print("The smallest value is: ", containerList[3])

sumOfList = containerList[0] + containerList[1] + containerList[2] + containerList[3]
print("The sum of the list is: ", sumOfList)

