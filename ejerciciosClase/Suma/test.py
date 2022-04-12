from numero import Numero
import unittest 
class TestMusic(unittest.TestCase):
    def test_suma(self):
        p=Numero(3)
        q=Numero(4)
        self.assertEqual(p.suma(q), 7)

    if __name__=="__main__":
        unittest.main()
