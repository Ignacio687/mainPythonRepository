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
        row = self.NAPIRS(column)
        self.board[row][column] = self.turn
        self.verifyLine(row)
        self.verifyColumn(column)
        self.verifyDiagonalToTheRigth(row, column)
        self.verifyDiagonalToTheLeft(row, column)
        self.turn = 1 - self.turn
    
    def verifyLine(self, row):
        tokenCounter = 0
        for column in range(0,8):
            tokenCounter = tokenCounter+1 if self.board[row][column] == self.turn else 0
            if tokenCounter > 3: raise WinnerException
    
    def verifyColumn(self, column):
        tokenCounter = 0
        for row in range(0,8):
            tokenCounter = tokenCounter+1 if self.board[row][column] == self.turn else 0
            if tokenCounter >= 4: raise WinnerException
    
    def verifyDiagonalToTheRigth(self, row, column):
        tokenCounter = 0
        startPoint = (column-row) if column-row > 0 else (row-column)
        for counter in range(startPoint, 8):
            tokenCounter = tokenCounter+1 if self.board[counter-startPoint if column-row > 0 else counter][counter-startPoint if column-row < 0 else counter] == self.turn else 0
            if tokenCounter >= 4: raise WinnerException
    
    def verifyDiagonalToTheLeft(self, row, column):
        tokenCounter = 0
        startPoint = (column+row) if column+row <= 7 else (row-(7-column))
        for counter in range(startPoint, -1 if column+row <= 7 else 8, -1 if column+row <= 7 else 1):
            tokenCounter = tokenCounter+1 if self.board[counter if column+row > 7 else startPoint-counter][counter if column+row <= 7 else 7-(counter-startPoint)] == self.turn else 0
            if tokenCounter >= 4: raise WinnerException