import random

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

def generate_board(solver,M=9,N=9,fill=20):
    import pdb; pdb.set_trace()
    assert M%3==0 and N%3==0, "Dimensions must be divisible by 3"
    board = [[0 for j in range(1,N+1)] for i in range(1,M+1)]
    f = 0
    while f < fill:
        i = random.randint(0,M-1)
        j = random.randint(0,N-1)
        val = random.randint(1,M)
        board[i][j] = val
        if solver(board):
            f += 1
            continue
        board[i][j] = 0
    return new_board

def transform_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                board[i][j] = 0
            else:
                board[i][j] = int(board[i][j])
    return board
    
if __name__ == "__main__":
    from pprint import pprint
    pprint(transform_board(board2))
    #pprint(generate_board(9,9))