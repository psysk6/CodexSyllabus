#Headings of each row
headingRow = "  1 2 3 4"
#array of numbers we are going to print out in the grid formation.
rows = ["A","B","C","D"]
board = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
print(headingRow)

i = 0 #iterator for characters on the board
j = 0 #iterator for the numebr of rows 
while(i < len(rows) and j < len(board)):
    row = ("{0} {1} {2} {3} {4}").format(rows[i],board[j],board[j+1],board[j+2],board[j+3])
    print(row)
    #need to know what to increment i an j with
    i += 1
    j += 4
