def validation(board,row,col,number):
    # check entire row and col
    for i in range(9):
        if board[row][i]==number:
            return False
    for i in range(9):
        if board[i][col]==number:
            return False
    # direct mapping
    block_start_row = {0:0,1:0,2:0,3:3,4:3,5:3,6:6,7:6,8:6}
    block_start_col = {0:0,1:3,2:6,3:0,4:3,5:6,6:0,7:3,8:6}
    # index calculation
    block_index = (row//3)*3 + (col//3)
    # starting row and col for 3x3 grid
    start_row = block_start_row[block_index]
    start_col = block_start_col[block_index]
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j]==number:
                return False
    return True

def isEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None

def solveSudoku(board):
    empty = isEmpty(board)
    if empty is None:
        return True
    row, col = empty
    for i in range(1,10):
        if validation(board,row,col,i):
            board[row][col] = i
            if solveSudoku(board):
                return True # if done return from here 
            board[row][col] = 0 # if not remove the current number and initial 0 and backtrack
    return False # for no solution

def print_board(board):
    for i in board:
        print(" ".join(str(num) for num in i ))
        
def main():
    filename = "F:\MDU\DVA340\Assignment 1\Assignment 2 sudoku.txt"
    with open(filename, 'r') as file:
        line = file.readlines()
        sudoku_board = []
        current_sudoku_board = []
        for i in line:
            i = i.strip()
            if i.startswith('SUDOKU'):
                if current_sudoku_board:
                    sudoku_board.append(current_sudoku_board)
                current_sudoku_board = []
            elif i.isdigit():
                current_sudoku_board.append([int(j) for j in i])
        if current_sudoku_board:
            sudoku_board.append(current_sudoku_board)
    for idx, sudoku in enumerate(sudoku_board):
        print(f"SUDOKU {idx + 1}:")
        if solveSudoku(sudoku):
            print_board(sudoku)
        else:
            print("No solution exists.")
        print()
        
if __name__ == '__main__':
    main()