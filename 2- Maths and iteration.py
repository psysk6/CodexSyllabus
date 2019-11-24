#This lesson will teach some very basic maths in python as well as how to use iteration: how to do an instruction several times over

#1 maths in python

#python is very useful for maths

#you can do maths very quickly in command line

#try it!
#1+1
#2*3 etc...

#there are also some other useful maths functions which  might not be immediately obvious

#// is integer divsion no matter what it will return an integer

#** can be used for indices i.e. 2**2 is 2 squared

#we can use brackets to say to do something first i.e. (1+1)*2 = 18

#2 iteration

#how do we do something several times?

#we can use iteration or recursion (I won't show you recursion just yet because its quite difficult to understand)

#one type of iteration is a for loop

#for loops are as follows

# for SomeVariable in range(x,y,z):

#x is the counter for the loop i.e. what were starting from

#y is what we're trying to get to

#z is the size of the step we take

#code after the semicolon : will execute for the number of times we specify

#for example the following code will print what you tell it to 5 times:

#for i in range(0,5,1):
    #print("your message here")
#try it below!:
#============================================================================================
##for i in range (1,10,2):
##    print(i)
##    print("hello")
    
    
#===================================================================================================

#if you simply add 1 paramater it will simply iterate up to that number for example:

# for i in range 10:

# i is our counter

#we can use the counter in our functions

# in the task above try printing i as well as your message!

#3 while loops
#while loops are a different kind of iteration

#while loops will keep iterating until a certain criteria is true

#in order to understand how a while loop works we first need to know the logical operators in python

#1. a > b = a is less greater than b
#2. a < b = a is smaller than b
#3. a >= b = a is greater than or equal to b
#4. a <= b = a is less than or equal to b
#5. a == b = a = b
#6. a != b = a does not equal b

#now we can make a simple while loop

#a while loop is structured as follows:
##a = 0                           #1: set your counter to a number to start with
##while a < 10:
##    print("doing something")
##    a += 1                      #add 1 to the counter

#the only real difference is we increment the counter ourselves
#try a while loop below:
#===================================================================================================
##i = 0 
##while(i<9):
##    print("dggdgdghshsye")
##    i=i+1
    
    
#===================================================================================================

#we can combine multiple selection statements together using AND and OR for example
#a = 1
#b = 2
#c = 5
#while a < b or b < c:
    #print("we are combining selections statments")
    #a+=1
    #b+=1
#============================================================================================================================================================================================

    


#how does this contribute to our game?
#we now have everything we need to print the board!

#if you think back to last time we were having to print it out line by line which was messy
#using a while loop we can make it much easier
#we first print out our number row like we did before:

# print(columns)
# then we can begin to print out the other stuff
# so we need to print out 4 rows
# each containing 5 characters
# the next character from Row
# and then the next 4 from the board array
# and we will perform these operations while our iterator for the board is less than the length of the board
# and while our row iterator less than the length of the rows array

#here's what we have:

board = [3, 1, 4, 7, 5, 1, 7, 6, 6, 0, 2, 5, 0, 4, 2, 3]
rows = ["A","B","C","D"]
columns = "  1 2 3 4"

#we already know how to print columns:
print(columns)

#so we need 2 variables

#I'm going to call them 
# i and j
# we set them to 0 to start with:
#i = 0
#j = 0

#we're saying that while i < lengh of the board and j < length of rows
#while i < len(board) and j < len(rows):

#we can then in that while loop print out the next row:
#while i < len(board) and j < len(rows):
    #NextRow = ("{0} {1} {2} {3} {4}").format(rows[j],board[i],board[i+1],board[i+2],board[i+3])

#this is the characther in rows at index j which starts at A and then the next 4 characters from 4
#we have printed 4 chars from row so we increment i by 4

#i+=4

#and we have printed 1 row so we increment j by 1

#j+=1

#try it below!
#===================================================================================================
i = 0
j = 0

while i < len(board) and j < len(rows):
    NextRow = ("{0} {1} {2} {3} {4}").format(rows[j],board[i],board[i+1],board[i+2],board[i+3])
    print(NextRow)
    i += 4 
    j += 1
    
#===================================================================================================
def printBoard():
    i = 0
    j = 0

    while i < len(board) and j < len(rows):
        NextRow = ("{0} {1} {2} {3} {4}").format(rows[j],board[i],board[i+1],board[i+2],board[i+3])
        print(NextRow)
        i += 4 
        j += 1
    



#next we'll think about functions and how to recycle code and use it again and again!











