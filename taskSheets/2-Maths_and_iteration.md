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

Now that we know how to do iteration we can start making loops.

### 2.3- While Loops
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

Try printing something with this loop...what happens?
~~~~
while(a < 10):
    print("something")

~~~~
