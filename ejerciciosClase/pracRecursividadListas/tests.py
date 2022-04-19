import unittest 
from classList import SearchList

class ValueSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.list = SearchList()
    def test_EmptyList(self):
        self.assertFalse(self.list.searchProcedural([], 2))
    def test_OneValue(self):
        self.assertTrue(self.list.searchProcedural([1], 1))
    def test_OneValueNotFound(self):
        self.assertFalse(self.list.searchProcedural([1], 2))
    def test_MultipleValues(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 12))
    def test_MultipleValues(self):
        self.assertFalse(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 18))


if __name__=='__main__':
    unittest.main()