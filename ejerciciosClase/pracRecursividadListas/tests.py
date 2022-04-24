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
    def test_MultipleValuesMiddle(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14,15], 7))
    def test_MultipleValuesMiddleRigth(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14,], 7))
    def test_MultipleValuesMiddleLeft(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14,], 6))    
    def test_MultipleValuesMax(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 12))
    def test_MultipleValuesMin(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 2))
    def test_MultipleValuesPosition0(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 1))
    def test_MultipleValuesFinalPosition(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 14))
    def test_MultipleValuesMixSliceMax(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 9))
    def test_MultipleValuesMixSliceMin(self):
        self.assertTrue(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 5))
    def test_MultipleValuesNotFoundMax(self):
        self.assertFalse(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 18))
    def test_MultipleValuesNotFoundMin(self):
        self.assertFalse(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], -2))
    def test_MultipleValuesNotFoundInTheMiddle(self):
        self.assertFalse(self.list.searchProcedural([1,2,3,4,5,6,7,8,9,10,12,14], 13))

if __name__=='__main__':
    unittest.main()