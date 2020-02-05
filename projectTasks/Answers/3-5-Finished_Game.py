import random


#A function to reveal the square the user has selected
#revealedBoard- the board the user is playing on.
#board- order of each of the characters
def revealSquare(revealedBoard,board,index):
   revealedBoard[index] = board[index]
   return revealedBoard


#A function to change the board with an input character i.e. with a space to clear the board.
#changes the character at that index to the specified character.
def updateBoard(board,coord1,coord2,character):
   board[coord1] = character
   board[coord2] = character
   return board

#function to calculate where the coordinate is on the board
#row: string containing the user's input row
#column: the user's input for which column they wish to reveal
def calculateIndex(row,column):
   #call upper to make sure that the character is upper case
   row = row.upper()
   #initialise index to 0 
   index = 0
   #block which adds the corresponding number depending on which row the user has selected
   if row == "A":
      index += 0
   elif row == "B":
      index += 4
   elif row == "C":
      index += 8
   else:
      index += 12

   #testing column adds to the index depending on the user's column input
   if column == 1:
      index += 0
   elif column == 2:
      index += 1
   elif column == 3:
      index += 2
   elif column == 4:
      index += 3
   return index 



#get and check the user's row selection
def getRow():
   #list of valid rows
   validRows = ["A","B","C","D"]
   validRow = False
   #continuously test if the row is valid
   while not validRow:
      InputRow = input("enter row:")
      if InputRow.upper() in validRows:
         print("valid row")
         validRow = True 
      else:
         print("invalid row")
   return InputRow

#get and check the user's column selection
def getColumn():
   #test input for column
   validColumn = False
   while not validColumn:
      try:
         inputColumn = int(input("Enter column between 1-4:"))
      except ValueError:
         print("Invalid column")
      else:
         if(inputColumn > 4 or inputColumn < 1):
            print("Error: column must be between 1 and 5")
         else:
            print("Valid column")
            return inputColumn
      


#function which handles the user input into the program
def getBoardCoords(board):
   validIndex = False
   index = 0
   while not validIndex:
      row = getRow() #get user's row input
      column = getColumn() #get user's column input
      index = calculateIndex(row,column) #use row and column to calculate the index of board 
      #check that it's an unrevealed square
      if board[index] != '*':
         print("Error: invalid move")
         continue
      else:
         print("Valid index")
         return index



#function to initialise the game with the user's inputs
def StartGame(board):
    Moves = 0
    completedBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    revealedBoard = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    
    
    while revealedBoard != completedBoard:
         #print board
         printBoard(revealedBoard)

         #get the user's input     
         coord1 = getBoardCoords(revealedBoard)
         #reveal the user's selection         
         revealedBoard = revealSquare(revealedBoard,board,coord1)
         printBoard(revealedBoard)
      
         #get the second coordinate
         coord2 = getBoardCoords(revealedBoard)
         #reveal the user's selection
         revealedBoard = revealSquare(revealedBoard,board,coord2)
         printBoard(revealedBoard)

         #test if the 2 characters match
         if revealedBoard[coord1] == revealedBoard[coord2]:
            print("Success! you found a matching pair")
            #add blank space to indicat the pair match and have been cleared
            revealedBoard = updateBoard(revealedBoard,coord1,coord2," ")
         #else: reset the board
         else:
            print("unlucky, they didn't match")
            #add asterisk to reset the board
            revealedBoard = updateBoard(revealedBoard,coord1,coord2,"*")
         Moves += 1
         
    print("victory in", Moves, "moves!")

#function to get user's choice at the start menu- abstract can be reimplemented.     
def getUserChoice():
    validChoice = False
    while not validChoice:
       try:
          choice = int(input("Enter your choice:"))
       except ValueError:
          print("Error")
       else:
          return choice

#procedure to print the welcome message on the screen
def displayIntroScreen():
    print("Welcome to Sam and Dekarnye's matching pairs game!")
    print("1- Start a new random game")
    print("2- Start the training game")
    print("3- Exit the game")


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

#Executes on startup
def main():
   displayIntroScreen()
   choice = getUserChoice()

   board = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
   #if random game
   if choice == 1:
      print("Starting a random game...")
      random.shuffle(board)
      StartGame(board)
   #if training game
   elif choice == 2:
      print("Starting the training game...")
      StartGame(board)
   elif choice == 3:
       exit(0) 
   
   
main()
