class NoAvailablePositionException(Exception):
    pass
class TieException(Exception):
    pass
class WinnerException(Exception):
    pass

class FourInRow():
    
    def __init__(self):
        self.board = [['' for i in range(0,8)]for e in range(0,8)]
        self.turn = 0
    
    def resetBoard(self):
        self.board = [['' for i in range(0,8)]for e in range(0,8)]
    
    def NAPIRS(self, column):       # (NAPIRS) Next available position in column selector
        if self.board[0][column] != '':
            raise NoAvailablePositionException
        for row in range(1,8):
            if self.board[row][column] != '':
                return row -1
        return row
    
    def insertToken(self, column):
        self.board[self.NAPIRS(column)][column] = self.turn
        self.turn = 1 - self.turn