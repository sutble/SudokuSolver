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


class SudokuSolver:

    def __init__(self):
        pass

    def row(self,i,j,s):
            for k in range(0,self.N):
                val = self.board[i][k]
                if val in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and  val in s:
                        s.remove(val)

    def column(self,i,j,s):
        for k in range(0,self.M):
            val = self.board[k][j]
            if val in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and val in s:
                s.remove(val)
    def subbox(self,i,j,s):
        si = i//3
        sj = j//3
        for ki in range(si*3,si*3+3):
            for kj in range(sj*3,sj*3+3):
                val = self.board[ki][kj]
                if val in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and  val in s:
                    s.remove(val)

    def get_possible_values(self,i,j):
        s = set()
        s.update(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.row(i,j,s)
        self.column(i,j,s)
        self.subbox(i,j,s)
        return sorted(list(s))

    def next(self,i,j):
        return (i,j+1) if j < self.N-1 else (i+1,0)

    def solve(self,board):
        self.board = board
        self.M = len(board)
        self.N = len(board[0])
        return self._solver(0,0)
    
    def _solver(self,i,j):
            if(i == self.M-1 and j == self.N-1):
                if self.board[i][j] != '.':
                    return True
                else:
                    values = self.get_possible_values(i,j)
                    if values:
                        self.board[i][j] = values[0]
                        return True
                    return False
            if self.board[i][j] != '.':
                ni,nj = self.next(i,j)
                return self._solver(ni,nj)
            values = self.get_possible_values(i,j)
            v = 0
            finished = False
            while v < len(values) and not finished:
                value = values[v]
                self.board[i][j] = value
                ni,nj = self.next(i,j)
                finished = self._solver(ni,nj)
                v += 1
            if finished:
                return True
            else:
                self.board[i][j] = '.'
                return False
        
print(SudokuSolver().solve(board))
print(board)


    
