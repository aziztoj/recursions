def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        row_str = ""
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row_str += "| "
            val = board[r][c]
            row_str += (str(val) if val != 0 else '.') + ' '
        print(row_str)

def valid_digit_for_cell(board,row,col):
    if board[row][col] == 0:
        for i in range(1,10):
            if i in board[row]:
                continue
            for x in range(0,9):
                if i == board[x][col]:
                    break
            box_row = (row//3)*3
            box_col = (col//3)*3
            absent = True
            for r in range(box_row, box_row+3):
                for c in range(box_col, box_col+3):
                    if board[r][c] == i:
                        absent = False
            if absent == True:
                return i
    return board[row][col] 

def find_empty(board,emptylist):
    for n in range(0,9):
        for m in range(0,9):
            if board[n][m] == 0:
                emptylist.append([n, m])
    return emptylist            

# Alternative implementation for valid_digit_for_cell(board,row,col) where the sudoku number to check is passed to the function
def is_valid(board,row,col,num):
    
        for n in range(0,9):
            if board[row][n] == num:
                return False
        for n in range(0,9):
            if board[n][col] == num:
                return False
        box_row = (row//3)*3
        box_col = (col//3)*3
        for n in range(0,3):
            for m in range(0,3):
                if board[box_row+n][box_col+m] == num:
                    return False
        return True 

def solve(board):
    emptylist = []
    # Call find_empty to generate the list of empty spots on the board
    find_empty(board,emptylist)
    if not emptylist:
        return board
    # Extract the first empty spot from the list
    first_row = emptylist[0][0]
    first_col = emptylist[0][1]
    # Define base case: if the list is empty -> board is solved - what gets returned?
    
    # Copy and adapt the logic from valid_digit_for_cell(board,row,col)
    # For the identified first empty spot from the list, calculate the valid number
    # When a valid number has been found, call the same function again
    if board[first_row][first_col] == 0:
        for n in range(1,10):
            if is_valid(board,first_row,first_col,n):
                board[first_row][first_col] = n
                solve(board)

                board[first_row][first_col] = 0  
    return board
            

    # With the current board, there is no chance for a number to be invalid and we don't need to worry about backtracking/undoing yet
    
    # Once this code works, think about what would have to change or add if we needed to support 
    # multiple valid numbers for a single spot, and being able to undo a choice and go back to try another number

board = [                                                                   
    [5, 3, 4, 6, 0, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 0, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 0, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 0, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [0, 4, 5, 2, 8, 6, 1, 7, 9]
]

print_board(board)
# print(valid_digit_for_cell(board,8,2))

# emptylist = []
# find_empty(board,emptylist)
# print("there is an empty space at [row, column]", find_empty(board,emptylist))
# print(valid_digit_for_cell(board,8,6))

# row = 0
# col = 0

# for x in range(0,len(emptylist)):
#     for y in range(0,2):
#         if y == 0:
#             row = emptylist[x][y]
#         else:
#             col = emptylist[x][y]
#     print(row)
#     print(col)
#     board[row][col] = valid_digit_for_cell(board,row,col)

# print_board(board)
print()
print_board(solve(board))