
listTest = [1,"Hello",32,"Goodbye","Testing"]
'''
for element in listTest:
    indexOfOurObject = listTest.index(element)
    #print("We are currently on element: ",element,"  - In our listTest, meaning we have gone through the loop ",indexOfOurObject,"Times")
    listTest[indexOfOurObject] = "I changed it"
    print(listTest)
'''
'''
for whatever in range(20):
    if whatever == 5:
        print(whatever)
    if whatever == 10:
        print(whatever)
    if whatever == 15:
        print(whatever)
'''
'''
Make 2 lists with any values,
using a for loop, print out all the values in both lists
'''

FirstList = ["x","y","z"]
SecondList = [1,2,3]
index = 0

'''
for element in FirstList:
    print(FirstList[index])
    print(SecondList[index])
    index = index + 1
'''

for element in FirstList:
    print(FirstList[FirstList.index(element)])
    print(SecondList[FirstList.index(element)])


'''
Create a list with any values.
Make 2 copies of that list with a for loop.
'''

'''list1 = [12,15,23,42,55,75,122,132,150,180,200]
Display the numbers that are divisble by 5 and if 
you find a number greater than 150 stop the loop.'''