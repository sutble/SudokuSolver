board = [[".",".",".","7",".",".","3",".","1"],
         ["3",".",".","9",".",".",".",".","."],
         [".","4",".","3","1",".","2",".","."],
         [".","6",".","4",".",".","5",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".","1",".",".","8",".","4","."],
         [".",".","6",".","2","1",".","5","."],
         [".",".",".",".",".","9",".",".","8"],
         ["8",".","5",".",".","4",".",".","."]]

board2 = [[".","8","9",".","4",".","6",".","5"],
          [".","7",".",".",".","8",".","4","1"],
          ["5","6",".","9",".",".",".",".","8"],
          [".",".",".","7",".","5",".","9","."],
          [".","9",".","4",".","1",".","5","."],
          [".","3",".","9",".","6",".","1","."],
          ["8",".",".",".",".",".",".",".","7"],
          [".","2",".","8",".",".",".","6","."],
          [".",".","6",".","7",".",".","8","."]]


def generate_board(M,N):
    assert M%3==0 and N%3==0, "Dimensions must be divisible by 3"

    '''
    How to generate a random sudoku board
    This is a good beginner level exercise into creating new code I believe
    We can google our way through this, but thats not the goal
    The goal is to create one

    First thought...
    Im saying is that previously the response was on "description" but it got changed to "comment" is there a reason for that?
    
    Next step get rid of the ugly as fuck dots and make them integers for crying out loud 
    
    '''


def transform_board(board):
    #new_board = [[j for j in range(1,10)] for i in range(1,10)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                board[i][j] = 0
            else:
                board[i][j] = int(board[i][j])
    return board
    
from pprint import pprint
pprint(transform_board(board2))
