'''
Write a program that asks the user which geometrical shape they wish to calculate with.
(Triangle, square, rectangle)
After the user has responded, depending on the shape,
ask for the length of all required sides to calculate the area and 
circumference of said shape. Return those values.'''

firstVariable = True
secondVariable = False
thirdVariable = True
if secondVariable or firstVariable:
    print("This is true")
elif firstVariable and secondVariable and thirdVariable :
    print("This is not true")
else:
    print("Third thing")


if firstVariable: print("This")

if firstVariable:
    pass
print("this")

thisIsMyList = ["car", 4, "blue"]
print(thisIsMyList)
print(thisIsMyList[1])
print(thisIsMyList[-1])
print(thisIsMyList[0:])

thisIsMyList.append("dog")
print(thisIsMyList)
thisIsMyList.remove(4)
print(thisIsMyList)

thisIsMyList.pop(0)
print(thisIsMyList)
del thisIsMyList[0]
print(thisIsMyList)
thisIsMyList.clear()
print(thisIsMyList)
thisIsMyList.insert(0,"Firstitem")
print(thisIsMyList)
thisIsMyList.insert(0,"New first item")
print(thisIsMyList)

thisIsMySecondList = thisIsMyList.copy()
print(thisIsMySecondList)

thisIsMySecondList.reverse()
print(thisIsMySecondList)

print(thisIsMySecondList.count("Firstitem"))

'''Write a program that asks for use input (Only numbers),
adds that input to a list, then returns to the user>
the largest number in the list, the smallest number,
and the sum of the numbers. (The list is only 4 items long)
'''

