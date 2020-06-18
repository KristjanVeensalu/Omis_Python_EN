'''
UserShapeInput = input("Enter the geometrical shape: ")
if UserShapeInput=="triangle":
    TriangleSideLenght= int(input("Please enter triangle side length: "))
    TriangleHeight= int(input("Please enter triangle height: "))
    print("Area of triangle is:" , TriangleSideLenght*TriangleHeight/2)   
    print("Circumference of a triangle is:", 2*TriangleSideLenght+TriangleHeight)
if UserShapeInput=="square":
    SquareSideLength=int(input("Please enter square side length: "))
    print("Area of a square is: ", SquareSideLength*SquareSideLength)
    print("Circumference of a square is: ", 4*SquareSideLength)
if UserShapeInput=="rectangle":
    RectangleFirstSideLenght=int(input("Plese enter rectangle first side lenght: "))
    RectagleSecondSideLenght=int(input("Please enter rectangle second side lenght: "))
    print("Area of a rectangle is: ", RectangleFirstSideLenght*RectagleSecondSideLenght)
    print("Circumference of a rectangle is: ",2*(RectangleFirstSideLenght+RectagleSecondSideLenght))
'''
import functions

programRuns = True
while programRuns:
    userInput = functions.getInput()
    IsItOk = functions.checkInput(userInput)
    print(IsItOk)
    while IsItOk != True:
        userInput = functions.getInput()
        IsItOk = functions.checkInput(userInput)
    if userInput == "triangle":
        functions.calculateTriangle()
        programRuns = False
    if userInput == "square":
        functions.calculateSquare()
        programRuns = False
    if userInput == "rectangle":
        functions.calculateRectangle()
        programRuns = False
    

#functions.enterShape()