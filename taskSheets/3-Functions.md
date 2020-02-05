# 3- Functions & Procedures

## 3.0 Introduction
In this lesson we'll be looking at how we use <strong>functions</strong> in python.

Functions can save us rewriting a lot of code and can allow us to create useful blocks of code which we can call at any time.

## 3.1 What is a procuedure?
A procedure in its simplest form is a named block of code which performs a specific task and be called throughout your program. 

They can take inputs, perform operations and return values

## 3.1 What is a function?
A function differs from a procedure as it must return take data for a procedure this is not mandatory.

A function can be seen as a machine which:

* takes inputs ->
* performs operations on or using these inputs ->
* returns an output.

in python the syntax is the same but the procedure may not return anything.

## 3.2 Structure of a function
A function in its simplest form is as follows:
~~~
def functionName(parameter1,parameter2...):
    do something...
    return something
~~~
the def indicates to python we are defining a function.
parameters are data values passed into the function.

The following is a very simple example of a function

~~~~
def HelloUser(username):
    sentence = print("Hello",username,"we hope you've enjoyed using this very simple function")
    return sentence
~~~~
this function takes the parameter username.
creates a variable called sentence and then returns to where it was called.

## 3.3 Calling a function
Now that we've defined a function how do we call it?

we call a function as follows:
~~~
functionName(parameter1,parameter2...)
~~~

When a function is called:
* python will go to the function. 
* Execute everything in the function block
* Return a value.
* Return to where function was called.

for example:
~~~~
def HelloUser(username): #<-- 2) Go to here. username = "Sam"  
    sentence = ("Hello {0}, we hope you've enjoyed using this very simple function").format(username) #<-- 3) Assign Sentence
    return sentence #<-- 4) We return Sentence HelloName now = sentence
HelloName = HelloUser("Sam") #<-- 1) Exection starts here <-- 5) We return to here
print(HelloName) #<-- 6) We print out helloName which now = sentence.
~~~~
the result:
~~~
>>> HelloUser("Sam")
"Hello Sam, we hope you've enjoyed using this very simple function"
~~~
Now we've created a very simple function we can use it wherever we want and we can use it for all sorts of different inputs.
~~~
HelloUser("Sam")
HelloUser("Steve")
HelloUser("Sally")
#etc...
~~~
This cuts down the amount of code we need to write.<strong>Yay for less work!</strong>

Use the above example to write a function which adds 100 to a number which you pass in.

Complete the code below:
~~~~
def AddOneHundred(Number):
    #code here

number = #something
print(number)
~~~~
## 3.3a - Something unusual about python.
One really unusual nuance of python is that unlike other languages which can only return one value from a function python can return several. This works as follows:
~~~
def modifyMultiple(value1,value2):
    value1 += 10
    value2 += 5
    return value1,value2

value1 = 10
value2 = 15

value1,value2 = modifyMultiple(value1,value2)

print(value1)
print(value2)
~~~
while this can be useful as a general good programming practice one function should do one thing only therefore we should use this feature as little as possible.

## 3.4 Inbuilt Functions.
Why reinvent the wheel? Python has a large number of inbuilt functions to make our lives easier

We've already used one particular function a load of times.

print() is an inbuilt function.

we will be using many more inbuilt functions throughout this project. I will be pointing out a few we can use later in the project.

## 3.5 Building our game: using functions.
Now that we understand functions we can actually start to build our program.

Last time we worked out how to print out our board.

this will be a fundamental part of our project.

We have a skeleton of our program which lays out all of the functions and methods we should implement
<!--teachers make sure students can find this-->

The functions and procedures we need to implement are:
* revealSquare(): Function to reveal the square the user has selected.
* updateBoard(): Function to change the board with an input character i.e. with a space when the user has found a matching pair to clear those squares.
* calculateIndex():Gets the user's row and column and calculates the array index of the user's input. 
* getBoardCoords():Function which handles the user input into the program.
* startGame(board):Function to initialise the game.
* getUserChoice():Get user's choice at the start menu.
* displayIntroScreen(): Procedure which prints out the title message.
* printBoard(board):Procedure to print the board in its current state.
* main(): Controls our flow through the program and initialises the game.

Today we will be focussing on:
* displayIntroScreen()
* printBoard()
* main()

if you remember the example from lesson 1 we are printing out the following:
~~~
Welcome to *yourNameHere*'s Matching Pairs Game!
1- Start a new random game
2- Start the training game
3- Exit the game
~~~

Can you find this in the skeleton program?

all of this is encapuslated in the displayIntroScreen() function

We want to make a call to this function.

Can you work out where the program goes first? 

Can you then work out where we should make our call displayIntroScreenFunction()?

Don't forget to put your name in the welcome message to claim this project as your own!

now we can try our printBoardFunction.

we want our printBoard function to work regardless of what's on the board. therefore we can use board as one of our parameters.

To do this:

1. Add your code from task 2 into the printBoardFunction

2. make sure that your program is printing the board parameter and the board is not defined in the printBoard Function.

The teachers will be there to help.

<strong>Try printing both the board and the masked board with the function.</strong>

Well done! now we know how to use functions we've made massive progress towards building our program. Next time we'll look at User Input and how to ensure that he user's input is checked to make sure it can't crash your program.

