'''
Recursive functions
'''
'''
def recursive(x):
    x+=1
    recursive(x)

recursive(0)
'''


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 1
print("The factorial of", num, "is", factorial(num))

def recursiveHello(x):
    if x == 0:
        print("Hello world!")
    else:
        print("Hello world!")
        recursiveHello(x-1)

recursiveHello(9)






