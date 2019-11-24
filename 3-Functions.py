import math
#Lesson 3 using functions

#up until this point we have just been writing out the code we need and if we need it again
#we write it again
#this session we will look at using functions which can be called again and again to perform
#the same action again in order to reduce the amount of code we need to write.

# they can also make code easier to read and fix bugs!

#1- basic structure of a function
# the basic structure of a function is as follows:

#def {function-name}({paramaters}):
    #do something
    #return soemthing if needed

#for example
def add1(number):
    number = number+1
    return number


a = 5
a = add1(a)
print("a is now",a)

b = 10
print(add1(b))

#then when you want to call a function you simply call the name and then the paramaters as follows:
a = add1(100)
print(a)


#python will read the function call and then go to where the function is defined do the stuff
#in the function and then return to where it was called

##def add1(number): <- 2) does whatever is in function
##    number = number+1 
##    return number <- 3) returns the result of the function

a = add1(100) #<-1) reads a function call <- 4) a is now assigned with the result of the function
print(a) # <- 5) we can now use the result of a in our code
 


#you could call it without assigning a variables

print(add1(1))

#or you could pass a variable in
a = 100
print(add1(a))

#task: make a function that will multiply a number by itself and then call it
#-------------------------------------------------------
def squared(a):
    a = a*a
             
    return a

a = 4
sentence = ("{0} squared is {1}").format(a,squared(a))
print(sentence)

def useSquare(a):

    sentence = ("{0} squared is {1}").format(a,squared(a))
    print(sentence)

for i in range(6):
    useSquare(i)




#-------------------------------------------------------

#it is possible with functions to return return multiple variables
#this will be useful in our program later on.

def squared1and2(a,b):
    a = a * a
    b = b * b
    return a,b

def SquareTwoNumbers(a,b):
    a = a * a
    b = b * b
    return a,b

a = 10
b = 20
a,b = SquareTwoNumbers(a,b)
print("returning two numbers:")
print(a)
print(b)


a = 10
b = 20

a,b = squared1and2(a,b)

print("a =",a)
print("b =",b)

#this is all you really need to know for this session but we can now do a lot more of our board game

#in order to make our game work we can begin to add simple functions to automate some stuff

#functions we need:
#a main function
#a function to display the board we made
#a function to run the game until it is finished
#a function to get the user's coordinate inputs
#a function to update the board
#a function to calculate the position of the user's input
#I've already defined the functions for you we just need to work out how to do them



