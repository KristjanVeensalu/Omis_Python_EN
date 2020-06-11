'''
Make a program that takes the user input that must be <100 and using a while loop store
every number starting from the input up to 100 in a list. The while loop also needs to check
if the input is correct.
'''





'''
Define a function called count that has two paramateres called FirstSequence and item.
Return the number of times the item occurs in the list.
For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
Then improve the function to be able to check two lists at once, so define a third paramater called SecondSequence.
'''


def count(FirstSequence,SecondSequence,item):
    occuranceNr = 0
    for x in FirstSequence:
        if x == item:
            occuranceNr +=1
    for x in SecondSequence:
        if x == item:
            occuranceNr +=1
    return occuranceNr

print(count([1,2,1,2],[1,2,4,5],2))


























'''
wordToGuessList = [0,"a","d"]
HasThisLetterBeenGuessed = "They have"
'''
'''
for x in wordToGuessList:
    if x == 0:
        HaveAllTheLettersBeenGuessed = "They have"
    else:
        HaveAllTheLettersBeenGuessed = "They have not"
if HaveAllTheLettersBeenGuessed == "They have":
    print("End the game")
else:
    print("The game keeps going")

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))


'''




def firstFunction(x):
    x = x*20
    emptyList = []
    emptyList.append(x)
    return emptyList

