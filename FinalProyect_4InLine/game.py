class NoAvailablePositionException(Exception):
    pass
class TieException(Exception):
    pass
class WinnerException(Exception):
    pass

class FourInrow:
    
    def __init__(self):
        self.board = [['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', '']]
        self.turn = 0
    
    def resetBoard(self):
        self.board = [['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', ''], 
                      ['', '', '', '', '', '', '', '']]
    
    def NAPIRS(self, column):       # (NAPIRS) Next available position in column selector
        for row in range[0,8]:
            if self.board[row][column] != '':
                return row - 1
        return row
    