import unittest
from game import FourInRow, NoAvailablePositionException, TieException, WinnerException
from parameterized import parameterized

class fourInRowTestCase(unittest.TestCase):

    def setUp(self):
        self.fourInRow = FourInRow()

    def test_boardGeneration(self):
        self.assertEqual(self.fourInRow.board, [['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', '']])

    def test_resetfourInRow(self):
        self.fourInRow.board = [['', '', '', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '1', ''], 
                                 ['', '', '', '', '', '0', '', ''], 
                                 ['', '', '', '', '1', '', '', ''], 
                                 ['', '', '', '0', '', '', '', ''], 
                                 ['', '', '1', '', '', '', '', ''], 
                                 ['0', '', '', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '', '0']]
        self.fourInRow.resetBoard()
        self.assertEqual(self.fourInRow.board, [['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', '']])
    
    @parameterized.expand([(0, 5), (1, 7),(2, 4), (3, 3), (4, 2), (5, 1), (6, 0), (7, 6)])
    def test_NextcolumnPositionSelector(self, column, row):
        self.fourInRow.board = [['', '', '', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '1', ''], 
                                 ['', '', '', '', '', '0', '', ''], 
                                 ['', '', '', '', '1', '', '', ''], 
                                 ['', '', '', '0', '', '', '', ''], 
                                 ['', '', '1', '', '', '', '', ''], 
                                 ['0', '', '', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '', '0']]
        self.assertEqual(self.fourInRow.NAPIRS(column), row)

    @parameterized.expand([(0,),(3,),(7,)])
    def test_NextcolumnPositionSelect_Exception(self, column):
        self.fourInRow.board = [['0', '', '', '0', '', '', '', '1'], 
                                 ['', '', '', '', '', '', '1', ''], 
                                 ['', '', '', '', '', '0', '', ''], 
                                 ['', '', '', '', '1', '', '', ''], 
                                 ['', '', '', '', '', '', '', ''], 
                                 ['', '', '1', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '', '']]
        with self.assertRaises(NoAvailablePositionException):
            self.fourInRow.NAPIRS(column)

    def test_InsertToken(self):
        self.fourInRow.insertToken(3)
        self.assertEqual(self.fourInRow.board, [['', '', '', '', '', '', '', ''], 
                                                ['', '', '', '', '', '', '', ''], 
                                                ['', '', '', '', '', '', '', ''], 
                                                ['', '', '', '', '', '', '', ''], 
                                                ['', '', '', '', '', '', '', ''], 
                                                ['', '', '', '', '', '', '', ''], 
                                                ['', '', '', '', '', '', '', ''], 
                                                ['', '', '', 0, '', '', '', '']])
    
    def test_turnChange(self):
        self.fourInRow.insertToken(4)
        self.assertEqual(self.fourInRow.turn, 1)
        self.fourInRow.insertToken(2)
        self.assertEqual(self.fourInRow.turn, 0)

    def test_InsertToken_Exception(self):
        self.fourInRow.board = [['', '', '', '', '', '', 1, ''], 
                                 ['', '', '', '', '', '', 0, ''], 
                                 ['', '', '', '', '', '', 0, ''], 
                                 ['', '', '', '', '', '', 1, ''], 
                                 ['', '', '', '', '', '', 1, ''], 
                                 ['', '', '', '', '', '', 1, ''], 
                                 ['', '', '', '', '', '', 1, ''], 
                                 ['', '', '', '', '', '', 0, '']]
        with self.assertRaises(NoAvailablePositionException):
            self.fourInRow.insertToken(6)

    def test_VerifyLineWinnerCondition(self, board, column):
        self.fourInRow.board = [    
                               ]
        with self.assertRaises(WinnerException):
            self.fourInRow.insertToken(0)

    def test_VerifyColumnWinnerCondition(self):
        self.fourInRow.board = [
                               ]
        with self.assertRaises(WinnerException):
            self.fourInRow.insertToken(0) 

    def test_VerifyDiagonalWinnerCondition(self):
        self.fourInRow.board = [
                               ]
        with self.assertRaises(WinnerException):
            self.fourInRow.insertToken(0) 
    
    # def test_tie(self):
    #     self.fourInRow.board = [['1', '1', '1', '', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1']]
    #     self.fourInRow.insertToken(3)
    #     with self.assertRaises(TieException):
    #         self.fourInRow.insertToken(5)
    
    # @parameterized.expand([([    ['', '', '', '', '', '', '', ''], 
    #                              ['', '', '', '', '', '', '', ''], 
    #                              ['', '', '', '', '', '', '', ''], 
    #                              ['', '', '', '', '', '', '', ''], 
    #                              ['', '', '', '', '', '', '', ''], 
    #                              ['', '', '', '', '', '', '', ''], 
    #                              ['', '', '', '', '', '', '', ''], 
    #                              ['', '1', '1', '1', '', '', '', '']
    #                         ], 0), 
    #                         ([   ['', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['0', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['0', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['0', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1']
    #                         ], 0),
    #                         ([   ['1', '1', '1', '1', '1', '1', '', '1'], 
    #                              ['1', '1', '1', '1', '1', '0', '1', '1'], 
    #                              ['1', '1', '1', '1', '0', '1', '1', '1'], 
    #                              ['1', '1', '1', '0', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1']
    #                         ], 6)])
    # def test_Winner(self, board, column):
    #     self.fourInRow.board = board
    #     with self.assertRaises(WinnerException):
    #         self.fourInRow.insertToken(column)

if __name__=='__main__':
    unittest.main()