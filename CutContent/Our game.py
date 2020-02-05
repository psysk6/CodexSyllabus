import random

def revealSquare(revealedBoard,board,index):
   #all this function does is changes the character in the game board with the actual char at that index
   revealedBoard[index] = board[index]
   return revealedBoard

def updateBoard(board,coord1,coord2,character):
   #function takes the index of whatever item we give it and replace it with the character we give it
   board[coord1] = character
   board[coord2] = character

def calculateIndex(row,column):
   row = row.upper()
   index = 0
   if row == "A":
      index += 0
   elif row == "B":
      index += 4
   elif row == "C":
      index += 8
   else:
      index += 12
   
   if column == 1:
      index += 0
   elif column == 2:
      index += 1
   elif column == 3:
      index += 2
   elif column == 4:
      index += 3
   return index 

def getBoardCoords(board):
   #this is the function which gets the user to input the coordinates for a square it returns the index of the char
   #we simply use 2 input statements one for row and one for column
   #then we can pass them into a function which calculates the index
   #index = calculateIndex(row,column)
   row = input("enter a row")
   column = int(input("enter a number"))
   index = calculateIndex(row,column)
   return index
   
def StartGame(board):
   Moves = 0
   completedBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
   revealedBoard = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
   PlayerOneScore = 0
   PlayerTwoScore = 0 
   #start game contains the main loop for the game
   player1Turn = True
   #we want the game to loop infinitely until it is finished

   #while revealedBoard != completedBoard:
         
      #1) revealing squares
         #we can first call our print board function to print the revealedBoard
         #we then call the input function which we will program next to take the inputCoord function which we will
         #program next
         #we assign the value the user has input to coord1 it will return the index of the character the user has selected
         #see the definition of getBoardCoords.
         #we then call revealSquare which takes the board Coordinate coordinate, our game board and the revealed board
         #see how this works in RevealSquare

         #we can then repeat this for the second char

         #we can then define a general update function which will change the character in the array with whatever character we choose
         #this will work for both if they clear the character and if it needs to be changed back to a *
         #all we need to do then is print a message for the user for when the game is over
   
   while revealedBoard != completedBoard:
      if player1Turn == True:
         print("Player 1 it is your turn")
      else:
         print("Player 2 it is your turn")
      print("Player 1 score =",PlayerOneScore)
      print("Player 2 score =",PlayerTwoScore)
      #print board
      printBoard(revealedBoard)
      print("Enter the first coordinate")
      coord1 = getBoardCoords(board)
      revealSquare(revealedBoard,board,coord1)
      printBoard(revealedBoard)
      print("Enter the second coordinate")
      coord2 = getBoardCoords(board)
      validCoord2 = False
      while validCoord2 == False:
         if coord2 == coord1:
            print("error cannot select the same coordinate twice")
            coord2 = getBoardCoords(board)
         else:
            validCoord2 = True
            
      revealSquare(revealedBoard,board,coord2)
      printBoard(revealedBoard)
      
      if revealedBoard[coord1] == revealedBoard[coord2]:
         print("these are a match")
         updateBoard(revealedBoard,coord1,coord2," ")
         if player1Turn == True:
            PlayerOneScore += 10
            player1Turn = False
         else:
            PlayerTwoScore += 10
            player1Turn = True
      else:
         print("these aren't a match")
         updateBoard(revealedBoard,coord1,coord2,"*")
         if player1Turn == True:
            player1Turn = False
         else:
            player1Turn = True
         

   #--
   print("you won!")
         
         
def getUserChoice():
   pass

def displayIntroScreen():
    print("Welcome to Sam and Dekarnye's matching pairs game!")
    print("1- start a new random game")
    print("2- start the training game")
    print("3- exit the game")

#function to print the board in its current state
def printBoard(board):
   rows = ["A","B","C","D"]
   columns = "  1 2 3 4"
   print(columns)
   #print 4 and then new line
   i = 0
   j = 0
   while i < len(board) and j < len(rows):
       NextRow = ("{0} {1} {2} {3} {4}").format(rows[j],board[i],board[i+1],board[i+2],board[i+3])
       print(NextRow)
       i += 4
       j += 1
   

   
def main():
   
   displayIntroScreen()    
   board = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
   #we need to start with a call to the display intro screen function.
   #we can then make a call to the get input function to get an option 

   #UserChoice = {something}
   
   #now that we know what the user wants to do we can use selection to decide what the program does

   #i.e. if UserChoice == 1:
            
         #elif...
   #we want to load a random game if they press 1
   #or a practice game if the user presses 2
   #or we can simply close the application if the user presses 3

   #we can then go and work on our game function

   #for the training game we can just call the game with the board
   #for the random gme we need to randomise the order of the board
   #all we need to do for this is call board.shuffle()
   UserChoice = int(input("Select an option:"))
   if UserChoice == 1:
      random.shuffle(board)
      #random game
      StartGame(board)
   elif UserChoice:
      #training game
      StartGame(board)








main() #our program starts running from main
