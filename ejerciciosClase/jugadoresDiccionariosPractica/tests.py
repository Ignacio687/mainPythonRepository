import unittest 
from classPlayers import Players


class PlayersTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Players()
    def test_SinGanador(self):
        self.assertEqual(self.player.winner({}), [])
    def test_UnaSolaKey(self):
        self.assertEqual(self.player.winner({"Juan": 20}), ["Juan"])
    def test_UnicoGanador(self):
        self.assertEqual(self.player.winner({'Juan': 20, 'Lisandro': 40, 'Matías': 80, 'Tomás': 10, 'Ignacio': 50}), ['Matías'])
    def test_MultiplesGanadores(self):
        self.assertEqual(self.player.winner({'Juan': 80, 'Lisandro': 40, 'Matías': 80, 'Tomás': 10, 'Ignacio': 80}), ['Juan', 'Matías', 'Ignacio'])
    def test_Prueba1(self):
        self.assertEqual(self.player.winner({'Pepe': 20, 'Jose': 20,'Juan': 80, 'Lisandro': 40, 'Matías': 80, 'Tomás': 10, 'Ignacio': 80}), ['Juan', 'Matías', 'Ignacio'])


if __name__=='__main__':
    unittest.main()