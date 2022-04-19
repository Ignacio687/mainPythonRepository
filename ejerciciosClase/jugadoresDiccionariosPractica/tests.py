import unittest 
from classPlayers import Players

player = Players()
class PlayersTestCase(unittest.TestCase):
    def test_UnicoGanador(self):
        self.assertEqual(player.winner({'Juan': 20, 'Lisandro': 40, 'Matías': 80, 'Tomás': 10, 'Ignacio': 50}), ['Matías'])
    def test_MultiplesGanadores(self):
        self.assertEqual(player.winner({'Juan': 80, 'Lisandro': 40, 'Matías': 80, 'Tomás': 10, 'Ignacio': 80}), ['Juan', 'Matías', 'Ignacio'])
    def test_SinGanador(self):
        self.assertEqual(player.winner({}), [""])

if __name__=='__main__':
    unittest.main()