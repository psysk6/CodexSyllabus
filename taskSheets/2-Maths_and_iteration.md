# 2- Maths and Iteration

## 2.0 Introduction
This lesson we will learn some more useful stuff which will help us build up to building our game. 

We will learn how we can do maths in python as well as how we can perform iteration- performing instructions or procedures several times.

We will then be looking to improve how we print our board using iteration.

## 2.1 Maths in Python
Python is very useful for maths.

The basic operators are:

* **+** Addition
* **-** Subtraction
*  \*  Multiplication
* /  Division 

You can do calculations straight from straight from the command line.
~~~
>>> 1+1
2
>>> 100-1
99
>>> 12*100
1200
>>> 14/2
7.0
~~~
 
## 2.1 A- Further Maths 
The examples above are fairly straightForward but there are some more useful mathematical operations we can use to do more interesting stuff. For example:

* ** Power- for example 2^3 = 2*2*2 = 8
* // Integer division- this will return an integer regardless of the result i.e. 7 / 2 would return 3.5 but 7 // 2 returns 3.
*  += add a value to the value stored in a variable for example:
~~~
>>> a = 20
>>> a += 1
>>> print(a)
21
~~~


Brackets can be used to indicate priority i.e. 

~~~
2*(3+4) = 
2 * 7 = 
14
~~~

## 2.2 Comparisons 
One of the most important and useful programming concepts is how we can compare 2 values like we do in maths.

i.e. is 4 less than 5
is 100 greater than or equal to 1000 etc.

As you'll see this is hugely important in iteration.

The comparative operators in python are:
* a \> b  a is greater than b
* a < b  a is less than b
* ==  a is equal to b 
* != a does not equal b
* <= a is less than or equal to b
* \>= a is greater than or equal to b

~~~~
>>> a = 100
>>> b = 1000
>>> a > b
False
>>> a < b
True
>>> a == b
False
>>> a != b
True
>>> a <= b
True
>>> a >= b
False
~~~~
## 2.2a Combining conditions
We can use multiple conditionals at once using AND and OR.

* AND: if both conditions are true overall the statement is true.
* OR: if one or both of the conditions are true it is true over all.

~~~~
>>> a and a or b
True
>>> a = 100
>>> a > 50 and a != 60
True
>>> a > 50 and a != 100
False
a > 100 or a != 101
True
a == 99 or (a/2) >= 50
True
~~~~

Now that we know how to test conditions we can start making loops.

## 2.3- While Loops
A while loop literally means keep looping while a certain criteria has not been reached. for example:

~~~~
while(a < 10):
    #do something...
~~~~
This literally means while a does not equal 10 keep doing whatever is in the loop. 

Note python is what is known as a 'white space sensitive' language so everything indented 4 spaces after the loop will be performed in the loop.
~~~~
while(a < 10):
    #This is in the loop
    #This is also in the loop
    #So is this
#but not this 
~~~~
<!--teachers at this point might want to show students how to refator their code.-->
Try printing something with this loop...what happens?
~~~~
while(a < 10):
    print("something")
~~~~
You'll notice it loops infinitely.

you can press ctrl+c to stop it.

It loops infinitely because we don't modify **a** therefore our exit criteria (a < 10 is never true so we don't exit the loop.)

to fix this in our loop we have to add 1 to a every iteration.

Now try it with the line to increment a:
~~~~
while(a < 10):
    print("something")
    #now we are incrementing a:
    a+=1
~~~~

it should now execute 10 times and then exit successfully!
~~~
>>> a = 0
>>> while(a < 10):
	print("something")
	a+=1

something
something
something
something
something
something
something
something
something
something
>>> 
~~~~

## 2.4- For Loops

For loops are slightly different from while loops. 

A for loop is structured as follows


for SomeVariable in range(x,y,z):

* **SomeVariable** is the number we start at conventionally this is usually called i or j though it doesn't have to be.

* **x** is the counter for the loop i.e. what were starting from

* **y** is what we're trying to get to

* **z** is the size of the step we take

for example:
~~~~
#i is 0
#counting to 5
#in steps of 1
for i in range(0,5,1):
	print("iteration number:",i)

iteration number: 0
iteration number: 1
iteration number: 2
iteration number: 3
iteration number: 4
>>> 
~~~~

In python it is generally acceptable to just pass one variable in, this will  be the number we are trying to get to i.e. the following code produces the same output as above.

~~~~
for i in range(5):
	print("iteration number:",i)
iteration number: 0
iteration number: 1
iteration number: 2
iteration number: 3
iteration number: 4

~~~~

## Applying this to our game: iteratively printing the board.

Last time we learned how to print the board using format print statements.

It gives us the output we and it works fine but there's a better way we can do this.



<!--this needs updating-->
~~~~
#Headings of each row
headingRow = "  1 2 3 4 "
#array of numbers we are going to print out in the grid formation.
board = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
print(headingRow)
#row A
row = ("A {0} {1} {2} {3}").format(board[0],board[1],board[2],board[3])
print(row)

#row B
row = ("B {0} {1} {2} {3}").format(board[4],board[5],board[6],board[7])
print(row)

#row C
row = ("C {0} {1} {2} {3}").format(board[8],board[9],board[10],board[11])
print(row)

#row D
row = ("D {0} {1} {2} {3}").format(board[12],board[13],board[14],board[15])
print(row)
~~~~

 Now we can think about how to print them iteratively.



We will start with the same stuff as we had before
* The headings row *headingRow*
* the of letters which are displayed at the beginning of each row.
* the board itself
~~~
#Headings of each row
headingRow = "  1 2 3 4"
#array of letters we are going to print out in the grid formation.
rows = ["A","B","C","D"]
board = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
~~~
As with the first section we can print the heading row.
~~~
print(headingRow)
~~~
However instead of simply printing 4 times we want a while loop.

~~~
while(condition(s)):
    row = ("{0} {1} {2} {3} {4}").format(rows[something],board[something],board[something],board[something]
    print(row)
~~~
What would our conditions be? considering that we want to print out all of the board row letters and all of the characters in the board?

Here's a hint below I've created 2 variables which are set to 0:
* characterNumber
* rowNumber 

A side note the function len() is very useful and can be used to find the length of an array for example:
~~~
>>> a = [1,2,3]
>>> len(a)
3
~~~
with this in mind try to complete the code below:
~~~
#Headings of each row
headingRow = "  1 2 3 4"
#array of numbers we are going to print out in the grid formation.
rows = ["A","B","C","D"]
board = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
print(headingRow)

characterNumber = 0 #iterator for characters on the board
rowNumber = 0 #iterator for the numebr of rows 
while(*something* < len(*something*) and something < len(something)):
    row = ("{0} {1} {2} {3} {4}").format(rows[something],board[something],board[something+1],board[something+2],board[something+3])
    print(row)
    #need to know what to increase rowNumber and characterNumber by considering we print out 1 from rows and 4 board
    c += *something*
    j += *something*
~~~

Once finished the code should output the same as before. But now we are using iteration which makes for a more elegant piece of code.

 Throughout our project we will use iteration to perform a variety of different tasks.

 Next time we will be learning all about functions and how they can be useful in reusing code and making code easier to read as well as beginning to see how our whole project is going to fit together.