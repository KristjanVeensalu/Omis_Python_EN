import os
'''
f = open("newfile.txt", "a")
'''
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
'''
'''
f.write("writing in my new file\n")
f.write("Writing in it again\n")
f.write("Writing in it again\n")
f.write("Writing in it again\n")
f.write("Writing in it again\n")
f.write("Writing in it again\n")
f.close()
'''
'''
f = open("newfile.txt", "r")

for x in f:
    x = x + "test"
    print(x)

'''
#f.close()

'''
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("Does not exist")
'''
'''
Write a program that takes user input and writes it in a file.
When the user inputs X the program will end.
When the user inputs R the contents of the file will be read back to them and the program will end.
'''
















ProgramIsRunning = True

while ProgramIsRunning:
    UserInput = input("Enter text>>> ")
    f = open("newfile.txt", "a")
    if UserInput != "X" and UserInput != "R":
        f.write(UserInput + "\n")
        f.close()
    elif UserInput == "X":
        f.close()
        ProgramIsRunning = False
    else:
        f.close()
        f = open("newfile.txt", "r")
        for x in f:
            print(x)
        f.close
        ProgramIsRunning = False

