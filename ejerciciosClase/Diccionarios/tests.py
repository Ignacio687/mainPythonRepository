import unittest 
from main import buscarRepetidos

class NumerosRepetidosTestCase(unittest.TestCase):
    def test_noSeRepiten(self):
        self.assertEqual(buscarRepetidos([1,2,3,4]), {1:1, 2:1, 3:1, 4:1})
    def test_cantRepetidos(self):
        self.assertEqual(buscarRepetidos([1,1,2,3,4,5,3,3,2,9]), {1:2, 2:2, 3:3, 4:1, 5:1, 9:1})

if __name__=="__main__":
    unittest.main()