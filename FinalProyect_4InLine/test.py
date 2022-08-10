import unittest
from game import FourInrow, NoAvailablePositionException, TieException, WinnerException
from parameterized import parameterized

class FourInrowTestCase(unittest.TestCase):

    def setUp(self):
        self.fourInrow = FourInrow

    def test_boardGeneration(self):
        self.assertEqual(self.fourInrow.board(), [['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', '']])

    def test_resetfourInrow(self):
        self.fourInrow.resetBoard()
        self.assertEqual(self.fourInrow.board(), [['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', ''], 
                                                   ['', '', '', '', '', '', '', '']])
    
    @parameterized.expand([(0, 2), (1, 0),(2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1)])
    def test_NextcolumnPositionSelector(self, column, row):
        self.fourInrow.board = [['', '', '', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '1', ''], 
                                 ['', '', '', '', '', '0', '', ''], 
                                 ['', '', '', '', '1', '', '', ''], 
                                 ['', '', '', '0', '', '', '', ''], 
                                 ['', '', '1', '', '', '', '', ''], 
                                 ['0', '', '', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '', '0']]
        self.assertEqual(self.fourInrow.NAPIRS(column), row)

    @parameterized.expand([(0,),(3,),(7,)])
    def test_NextcolumnPositionSelect_Exception(self, column):
        self.fourInrow.board = [['0', '', '', '0', '', '', '', '1'], 
                                 ['', '', '', '', '', '', '1', ''], 
                                 ['', '', '', '', '', '0', '', ''], 
                                 ['', '', '', '', '1', '', '', ''], 
                                 ['', '', '', '', '', '', '', ''], 
                                 ['', '', '1', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '', ''], 
                                 ['', '', '', '', '', '', '', '']]
        with self.assertRaises(NoAvailablePositionException):
            self.fourInrow.NAPIRS(column)

    # def test_InsertToken(self):
    #     self.assertEqual(self.fourInrow.insertToken(3), [['', '', '', '', '', '', '', ''], 
    #                                                       ['', '', '', '', '', '', '', ''], 
    #                                                       ['', '', '', '', '', '', '', ''], 
    #                                                       ['', '', '', '', '', '', '', ''], 
    #                                                       ['', '', '', '', '', '', '', ''], 
    #                                                       ['', '', '', '', '', '', '', ''], 
    #                                                       ['', '', '', '', '', '', '', ''], 
    #                                                       ['', '', '', '0', '', '', '', '']])
    
    # def test_turnChange(self):
    #     self.fourInrow.insertToken(4)
    #     self.assertEqual(self.turn(), 1)
    #     self.fourInrow.insertToken(2)
    #     self.assertEqual(self.turn(), 0)

    # def test_InsertToken_Exception(self):
    #     self.fourInrow.board = [['', '', '', '', '', '', '1', ''], 
    #                              ['', '', '', '', '', '', '0', ''], 
    #                              ['', '', '', '', '', '', '0', ''], 
    #                              ['', '', '', '', '', '', '1', ''], 
    #                              ['', '', '', '', '', '', '1', ''], 
    #                              ['', '', '', '', '', '', '1', ''], 
    #                              ['', '', '', '', '', '', '1', ''], 
    #                              ['', '', '', '', '', '', '0', '']]
    #     with self.assertRaises(NoAvailablePositionException):
    #         self.fourInrow.insertToken(6)
    
    # def test_tie(self):
    #     self.fourInrow.board = [['1', '1', '1', '', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1'], 
    #                              ['1', '1', '1', '1', '1', '1', '1', '1']]
    #     self.fourInrow.insertToken(3)
    #     with self.assertRaises(TieException):
    #         self.fourInrow.insertToken(5)
    
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
    #     self.fourInrow.board = board
    #     with self.assertRaises(WinnerException):
    #         self.fourInrow.insertToken(column)

if __name__=='__main__':
    unittest.main()