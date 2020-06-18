
def getInput():
    returnAbleInput = input("Enter the geometrical shape: ")
    return returnAbleInput

def checkInput(checker):
    try:
        if checker == "triangle" or checker == "rectangle" or checker == "square":
            return True
        else:
            return False
            print dfasdfg
    except:


def calculateTriangle():
    tryAgain = False
    while tryAgain != True:
        try:
            TriangleSideLenght= int(input("Please enter triangle side length: "))
            TriangleHeight= int(input("Please enter triangle height: "))
            areaOfTriangle= TriangleSideLenght*TriangleHeight/2
            circumferenceOfTriangle= 2*TriangleSideLenght+TriangleHeight
            print("The area is: ", areaOfTriangle)
            print("The circumference is: ", circumferenceOfTriangle)
            tryAgain = True
        except:
            print("That is not a number!")

def calculateRectangle():
    tryAgain = False
    while tryAgain!= True:
        try:
            RectangleSideA = int(input("Enter first side: "))
            RectangleSideB = int(input("Enter Second side: "))
            print("The area is: ", RectangleSideA * RectangleSideB)
            print("The circumference is: ", (RectangleSideB + RectangleSideA)*2)
            tryAgain = True
        except:
            print("That is not a number")


def calculateSquare():
    tryAgain = False
    while tryAgain!= True:
        try:
            squareSide = int(input("Enter the side: "))
            print("The area is: ", squareSide*squareSide)
            print("The circumference is: ", squareSide*4)
            tryAgain = True
        except:
            print("That is not a number")


'''
def enterShape():
    UserShapeInput=input("Enter the geometrical shape: ")
    while UserShapeInput!="triangle" and UserShapeInput!="rectangle" and UserShapeInput!="square":
        UserShapeInput=input("Enter the geometrical shape again: ")

    if UserShapeInput=="triangle":
        TriangleSideLenght= int(input("Please enter triangle side length: "))
        TriangleHeight= int(input("Please enter triangle height: "))
    areaOfTriangle= TriangleSideLenght*TriangleHeight/2
    circumferenceOfTriangle= 2*TriangleSideLenght+TriangleHeight
    return print(areaOfTriangle), print(circumferenceOfTriangle)

'''