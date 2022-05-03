import unittest
from classCoffeeMachine import CoffeeMachine

class CoffeMachineNewMachinePerTest(unittest.TestCase):
    def test_NoCoin(self):
        machine = CoffeeMachine(0,0,0)
        self.assertFalse(machine.coin())
    def test_Coin(self):
        machine = CoffeeMachine(0,0,0)
        self.assertTrue(machine.coin())
    def test_NoCoinCoffeRequest(self):
        machine = CoffeeMachine(0,1,1)
        self.assertEqual(machine.give,{"coins":0,"coffee":0,"sugarCoffee":0})
    def test_CoinNoRequest(self):
        machine = CoffeeMachine(1,0,0)
        self.assertEqual(machine.give,{"coins":1,"coffee":0,"sugarCoffee":0})
    def test_CoinCoffeRequest(self):
        machine = CoffeeMachine(1,1,0)
        self.assertEqual(machine.give,{"coins":0,"coffee":1,"sugarCoffee":0})
    def test_CoinCoffeesRequest(self):
        machine = CoffeeMachine(1,1,2)
        self.assertEqual(machine.give,{"coins":0,"coffee":1,"sugarCoffee":0})
    def test_CoinsNoRequest(self):
        machine = CoffeeMachine(3,0,0)
        self.assertEqual(machine.give,{"coins":3,"coffee":0,"sugarCoffee":0})
    def test_CoinsCoffeRequest(self):
        machine = CoffeeMachine(3,1,0)
        self.assertEqual(machine.give,{"coins":2,"coffee":1,"sugarCoffee":0})
    def test_CoinsCoffeesRequest(self):
        machine = CoffeeMachine(3,1,2)
        self.assertEqual(machine.give,{"coins":0,"coffee":1,"sugarCoffee":2})
    def test_CoinsCoffeesRequestExceeded(self):
        machine = CoffeeMachine(3,2,2)
        self.assertEqual(machine.give,{"coins":0,"coffee":2,"sugarCoffee":1})
    def test_CoinSugarCoffeRequest(self):
        machine = CoffeeMachine(1,0,1)
        self.assertEqual(machine.give,{"coins":0,"coffee":0,"sugarCoffee":1})
    def test_CoinsSugarCoffeRequest(self):
        machine = CoffeeMachine(3,0,1)
        self.assertEqual(machine.give,{"coins":2,"coffee":0,"sugarCoffee":1})
    def test_AmountCoffeeExceeded(self):
        machine = CoffeeMachine(7,3,4)
        self.assertEqual(machine.give,{"coins":1,"coffee":3,"sugarCoffee":3})

class CoffeMachineNewMachinePerTest(unittest.TestCase):
    def setUp(self):
        self.machine = CoffeeMachine()
    def test_FirstPetition():


if __name__=='__main:__':
    unittest.main()