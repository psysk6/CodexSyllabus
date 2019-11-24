#welcome to your first program this will teach you how to print to the output window and how to use variables

#this is what a print statement looks like:
#print("*your statement here*")
print("hello")
#try it below!:


#variables are just giving some data a name
#a = 1
#b = "a string"
#you can recall stuff in a variable any time 

#you can use print to print stuff stored in variables
#a = "your statement here"
#print(a)
#try it below:
#=========================================

#=========================================


#when printing stuff stored in variables you want them outside the quotes
#what if you wanted to print a statement and then something in a variable

#we can use + and , for this

#',' adds a space and then we can add our variable in afterwards
# a = "insert your name here"
#print("hello",a)
#print("the value of a is",a)

#try it below:
#=========================================
name = "Sam"
print("hello",name)
name="dekarnya"
print("hi",name)

#=========================================



#+ will not add the space in afterwards

#try the statement again with a + instead:
#=========================================

#=========================================

#this can work in the middle of a string as well:
#a = "*insert your name here*"
#print("hello",a,"how are you?"

#=================================================string .format====================================================================
#finally the fanciest method of printing variables in a string is the string.format() function

#you tell the function where you want to put the variable in the string using curley brackets {}

#a = ("hello{0}!).format("*your name here*")
#print(a)


#try it!:
#=========================================
name = "sam"
output = ("hello {0}").format("sam")
print(output)

name="dekarnya"
output=("how are you {0}?").format("dekarnya")
print(output)




#=========================================


#you can use several variables like this
#a = ("hello {0}, you are {0} years old!).format("*your name here*",*your age here*)

#try it!:
#=========================================

#=========================================


#=================================================The Matching Pairs Game====================================================================
#how does this contribute to us making our game?

#it's going to let us start to print out the rows of our board:
#we have our numbers row:

NumbersRow = "1 2 3 4 5"
#We have all of our columns
#And we have our rows:
Rows = ["A","B","C","D"]
#And we have all of the stuff in the board game:

board = [3, 1, 4, 7, 5, 1, 7, 6, 6, 0, 2, 5, 0, 4, 2, 3]
print(NumbersRow)
print(board)
row = ("{0} {1} {2} {3} {4}").format(Rows[0],board[0],board[1],board[2],board[3])
print(row)
row = ("{0} {1} {2} {3} {4}").format(Rows[1],board[4],board[5],board[6],board[7])
print(row)
row = ("{0} {1} {2} {3} {4}").format(Rows[2],board[8],board[9],board[10],board[11])
print(row)
row = ("{0} {1} {2} {3} {4}").format(Rows[3],board[12],board[13],board[14],board[15])
print(row)

#for now we can print out the numbers row

#Print(NumbersRow)

#however it's not straightforward to print out the rest of the board how we want
#next time we're going to look at iteration: how to perform an instruction several times using 'iteration'


