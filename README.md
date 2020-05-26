# Omis Python
Python and programming basics course.
<br></br>
<a href="https://www.omis.ee/course/python-2503-3004-40-kr_eesti/">Homepage</a>
<br></br>
Lecturer: Kristjan Veensalu
<br></br>
Email: kristjan.veensalu@gmail.com
<br></br>

<hr></hr>
Useful Links:
<ul>
	Python history and introduction
	<li>https://www.geeksforgeeks.org/history-of-python/</li>
	Python syntax
	<li>https://www.w3schools.com/python/default.asp</li>
	Input/Output
	<li>https://www.programiz.com/python-programming/input-output-import</li>
	Data types
	<li>https://docs.python.org/3/library/datatypes.html</li>
	If conditions
	<li>https://www.w3schools.com/python/python_conditions.asp</li>
	For and While loops
	<li>https://www.w3schools.com/python/python_while_loops.asp</li>
	<li>https://www.w3schools.com/python/python_for_loops.asp</li>
	Functions
	<li>https://www.w3schools.com/python/python_functions.asp</li>
	DateTime
	<li>https://www.w3schools.com/python/python_datetime.asp</li>
	Documentation
	<li>https://www.python.org/doc/</li>
</ul>
<hr></hr>
Homework
<br></br>
<ul>
	<li>Write a small drill program to learn the multiplication table</li>
	<li>1. It shows the user a simple mathematical exercise.</li>
	<li>2. The user inputs an anwser and the program checks if its correct.</li>
	<li>3. Then it tells the user if they are correct or not</li>#
	<li>4. This program has a total of at least 10 different exercises to choose from.</li>
<hr></hr>

![Pilt pythoni koodist](/assets/pilt.png)

Fixing bugs: 

The first goal in terms of debugging should be to start the program on the first attempt, ie the program code has been reviewed,
primary minor errors and slipups have been removed (syntax errors). To do this, read the program and make sure that:

- None of the variables have a keyword name
- at the end of the function (if, while, for, def) there is a colon:
- indentation is consistent. It is recommended to use only spaces or only tabs. Indents should be the same size.
- all strings have a start and end symbol (the latter tends to be omitted)
- all brackets are even
- the comparison is made with == and not = = and the assignment is with = and not ==

If the listed errors have already been found before starting the program, the check could be extended.
The following is a selection of questions that the tester is advised to ask while reading the program code
(by the way, this activity is officially called static testing):


1. Review the variables and their names:
- Whether an attempt is made to use the value of a variable before the variable occurs, ie is there any undervalued
variable on the right side of the attribution statement, expression, printout?
- Have you made a mistake while typing a variable name? Or have you written a variable in one place in the program
with a capital letter but with a lowercase letter for the same variable elsewhere?

2. Check the non function words:
- They must be in a different color in the IDLE editor - then they are spelled correctly. If not, check the word for an error.
- Also look at what features you use - maybe it's some of the features you are using to turn to a separate module (import math) etc.?

3. Avaldised ja andmetüübid - vaata üle nii aritmeetikaavaldised kui ka loogikaavaldised:
- Kas ühte lausesse või avaldisse on kokku sattunud sobivad andmetüübid? Arvude ja stringide koos kasutamine 
ei lõppe enamasti hästi. Arvuti ei saa arvutada "porgand" + 3.
- Kas kõik arvutamisel kasutatavad muutujad on peale sisestamist ka arvuks teisendatud?
- Kas sealjuures on kasutatud andme iseloomule sobivalt täisarvu (int()) või ujukomaarvu (float())?
- Kas tehete järjekord on õigesti määratud ja kas kasutatakse selleks piisavalt sulge?
- Kas võib tekkida jagamist nulliga?

3. Statements and data types - review both arithmetic and logical statements:
- Are there suitable data types in one sentence or expression? Using numbers and strings together
doesn't usually end well. The computer can not calculate "carrot" + 3.
- Have all variables used in the calculation been converted to numbers after entry?
- Are integers (int ()) or float () appropriate to the nature of the data?
- Has the order of actions been set correctly and are there enough brackets used?
- Could it be a divison by zero error?

4. Comparisons - Review the comparison operations in the logical statements:
- Are different things compared: for example, text and number? The computer can't decide if "carrots"> 3
- Is the algorithm correctly translated into comparison operations? For example, the result of using the characters < or <= may be different.
- Are the priorities for comparison work set correctly?
- Is the decimal variable compared to a specific number and then to the equal sign (==)?
Floating point numbers may not be accurate and are therefore unsuitable for comparison with an equal sign.


5. Errors in the program structure - review all language constructions (cycles, options)
- Do the indents correctly define the boundaries of the planned cycle and selection sentences?
- Whether the loops are essentially planned correctly - whether the content and logic of the while loop
is consistent and the value of the expression can become False? Are the variables used in the logic statement
values ​​changed within the cycle?
- Can the logic statement at the beginning of the cycle on the first iteration be True? Does the cycle start at all?

Good luck reading your code and finding errors on your own!

<hr></hr>
Student Githubs:
<ol>
	<li><a href="*">Anna Jakovleva</a></li>
</ol>
