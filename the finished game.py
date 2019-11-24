import random

def revealSquare(revealedBoard,board,index):
   revealedBoard[index] = board[index]
   return revealedBoard

def updateBoard(board,coord1,coord2,character):
   board[coord1] = character
   board[coord2] = character
   return board


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
   index = 0
   validRows = ["A","B","C","D"]
   validIndex = False
   while not validIndex:      
      validRow = False
      while not validRow:
         row = input("enter row:")
         if row.upper() in validRows:
            print("valid row")
            validRow = True 
         else:
            print("invalid row")
      validColumn = False
      while not validColumn:
         try:
            column = int(input("enter column 1-5:"))
         except ValueError:
            print("invalid column")
         else:
            if column > 5 or column < 1:
               print("error column must be between 1 and 5")
            else:
               print("valid column")
               validColumn = True
      index = calculateIndex(row,column)
      if board[index] != '*':
         print("error invalid move")
         continue
      else:
         print("valid index")
         return index




def StartGame(board):
    Moves = 0
    completedBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    revealedBoard = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    
    while revealedBoard != completedBoard:
         
         printBoard(revealedBoard)
          
         coord1 = getBoardCoords(revealedBoard)         
##         if revealedBoard[coord1] == " ":
##            print("you have already revealed this tile")
##            continue
         revealedBoard = revealSquare(revealedBoard,board,coord1)
         printBoard(revealedBoard)
         coord2 = getBoardCoords(revealedBoard)
##         if revealedBoard[coord2] == " ":
##            print("you have already revealed this tile")
##            continue
         revealedBoard = revealSquare(revealedBoard,board,coord2)
         printBoard(revealedBoard)

         if revealedBoard[coord1] == revealedBoard[coord2]:
            print("success! you found a matching pair")
            revealedBoard = updateBoard(revealedBoard,coord1,coord2," ")
         else:
            print("unlucky, they didn't match")
            revealedBoard = updateBoard(revealedBoard,coord1,coord2,"*")
         Moves += 1
    print("victory in", Moves, "moves!")
         
def getUserChoice():
    valid = False
    while not valid:
       try:
          choice = int(input("Enter your choice:"))
       except ValueError:
          print("Error")
       else:
          return choice

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
   choice = getUserChoice()

   board = [3, 1, 4, 7, 5, 1, 7, 6, 6, 0, 2, 5, 0, 4, 2, 3]
   if choice == 1:
      print("starting a random game...")
      random.shuffle(board)
      StartGame(board)
   elif choice == 2:
      print("starting the training game...")
      StartGame(board)
   elif choice == 3:
       exit(0) 
   
   














main()
