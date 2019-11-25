#Headings of each row
headingRow = "  1 2 3 4 "
#array of numbers we are going to print out in the grid formation.
board = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
rowLetters = ["A","B","C","D"]
print(headingRow)
#row A
row = ("{0} {1} {2} {3} {4}").format(rowLetters[0],board[0],board[1],board[2],board[3])
print(row)

#row B
row = ("{0} {1} {2} {3} {4}").format(rowLetters[1],board[4],board[5],board[6],board[7])
print(row)

#row C
row = ("{0} {1} {2} {3} {4}").format(rowLetters[2],board[8],board[9],board[10],board[11])
print(row)

#row D
row = ("{0} {1} {2} {3} {4}").format(rowLetters[3],board[12],board[13],board[14],board[15])
print(row)
