import unittest
from classCoffeeMachine import CoffeeMachine

class CoffeMachine(unittest.TestCase):
    def test_NoCoin(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.coins,0)
    def test_CountOfCoins(self):
        machine = CoffeeMachine(2)
        machine.insertCoin(3)
        self.assertEqual(machine.coins,5)
    def test_CoffeePetitionNoCoins(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.giveCoffe(0),'Not enough coins')
        self.assertEqual(machine.giveCoffe(1),'Not enough coins')
    def test_CoffePetition(self):
        machine = CoffeeMachine()
        machine.insertCoin(3)
        self.assertEqual(machine.giveCoffe(0),'Give Black Coffee')
        self.assertEqual(machine.giveCoffe(1),'Give Black Coffee Whit Sugar')
    def test_CoffeePetitionsMoreThanCoins(self):
        machine = CoffeeMachine()
        machine.insertCoin(1)
        machine.giveCoffe(1)
        self.assertEqual(machine.giveCoffe(0),'Not enough coins')
        self.assertEqual(machine.giveCoffe(1),'Not enough coins')
    





if __name__=='__main:__':
    unittest.main()