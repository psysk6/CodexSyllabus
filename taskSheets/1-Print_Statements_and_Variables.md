# 1- Print Statments and Variables
<!--teachers before the lesson should make sure that students can use Jupyter Notebook and have correct access to this note-->


## 1.0- Introduction
Hi, welcome to your first program! This will teach you the very basics of python: how to print to the output window and how to use variables.

Throughout this project you'll be learning the fundamental concepts of programming as well as learning how to make a very simple matching pairs game so you can see how the stuff you'vea just learned can be used.

~~~
Welcome to Sam and Dekarnye's Matching Pairs Game!
1- Start a new random game
2- Start the training game
3- Exit the game
Enter your choice:1

Starting a random game...

  1 2 3 4
A * * * *
B * * * *
C * * * *
D * * * *

Enter row:
~~~

Sounds like a lot right? We're gonna break it right down. 

## 1.1- A simple print statement
Firstly we need to know how to output to console. For this we use a print statement. The syntax for a print statement is as follows:
~~~
print("Hello World")
~~~
Try it Below:
<!--this will be an idle window in Jupyter-->
~~~
print("Hi my name is *your name*)
~~~

## 1.2- Storing stuff in variables
Variables are basically just a way of giving some data a name.

If we wanted to store something and use it later we use a variable.

A variable is structured as follows:

~~~
<variableName> = <Data>
~~~

For example: 

~~~
name = "Sam"
age = 20
~~~

### 1.2a- Variable Types
All variables have a type. This tells python what kind of data they contain. Some of the basic data types are:
* String- A string is a set of characters like a sentence or a name for example: 
  ~~~
  hello = "Hello World"
  name = "name"
  character = "a" 
  ~~~
* Integer- An integer is fairly self explanatory it contains an integer number. for example:
  ~~~
  NumberOfJobs = 2
  NumberOfPeople = 20
  ~~~
* Float- Much like an integer they contain a number however these can have decimal places for example:
  ~~~
  pi = 3.14
  percentComplete
  ~~~ 
* Booleans: these are variables which can be True or False. Just make sure your True or False start with a capital letter:
  ~~~
  IsTall = True
  OverEighteen = False
  ~~~
* Lists: Lists are a collection of data marked with square brackets i.e. they can contain any data.
    ~~~
    OneToTen = [1,2,3,4,5,6,7,8,9,10]
    Fruits = ["Apples","Pears","Tomatoes"]
    ~~~
    We can get individual elements from the array by using:
    ~~~
    list[element]
    ~~~
    for example:
    ~~~~
    Fruits[0]
    "Apples"
    ~~~~
We will be using array indexing later when we print our board out.
## 1.3- Printing Variables
We can print the stuff stored in variable by putting it in a print statement.

~~~
name = "Sam"
print("Sam")
~~~

Try Printing your own name below:
<!--teachers to make sure that all of the pupuls can do this-->
~~~

~~~

We can print a string and then print a variable using + or , for example:

~~~
Name  = "Sam"
print("hello my name is",Name)
~~~
the only difference between + and , is the , adds a space automatically.

you can use this to combine multple strings:
~~~
name = "Sam"
age  = "20"
print("hi my name is",name,"I am",age,"years old")
~~~
Try to print "hello my name is *your_name* I am *your_age*" below:
~~~

~~~
## 1.4 Using .format()
Now that we've learned how to insert stuff into our print statement we can do something a little more fancy!

*.format()* is a method.

Methods can act on and change variables.

They are in the format:

~~~
variable.method()
~~~

.format() will insert variables into a string.

a {x} indicates to the format function that it needs to insert one of the variables into it. 

for example:
~~~
Name = "Sam"
Age  = 20
FavoriteColour = "Blue"
output = ("Hello, my name is {0}. I am {1} years old. My 
favorite colour is {2}.").format(Name,Age,FavoriteColor)

print(output)
~~~

## 1.5 Applying what we've learned- Printing out the grid.
Great! Now we've learned everything we need to know to complete the first part of our game: printing out the board.

So what do we already have in our starter file?
<!--At this point teachers need to make sure that students are all correctly set up on Katiss-->
we have the first row i.e. the headings of the table in a variable called *headingRow*.
~~~
headingRow = "1 2 3 4 5"
~~~
We also have an array of numbers which will represent our grid. 
~~~
board = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
~~~
We also have a list of the letters we want to print out at the start of each row.
~~~
rowLetters = ["A","B","C","D"]
~~~

Just calling print on the board will print it in an array format. this isn't what we want.

~~~
print(board)
[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7,7]
~~~

Instead what we want to do is first print the heading row and then print 4 of the characters and then print the next on a new line. like:
~~~~
  1 2 3 4
A 0 0 1 1
B 2 2 3 3
C 4 4 5 5
D 6 6 7 7
~~~~
We're not going to worry about masking or the order of the characters just yet.

instead we're going to use *.format()*
to insert each character into the print statement.

Can you print out the board as it is above? complete the code below:

~~~~
headingRow = "1 2 3 4 5"
rowLetters = ["A","B","C","D"]
board = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
#first we want to print out the heading row
print(*something needs to go here*)
#then we want to print out the rows below. the first one has been done for you:
#print row A
row = ("{0} {1} {2} {3} {4}").format(rowLetters[0],board[0],board[1],board[2],board[3])
print(row)
#print row B
row = ()
print(row)
#print rows C and D...
~~~~

Print_Statements_and_Variables_Skeleton contains this code. submit on Kattis 

That looks great! and we've made a really good start, but we can do better! 
Next time we'll be looking at iteration and look at how we can improve printing out the board. 
