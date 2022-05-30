import unittest
from classCoffeeMachine import CoffeeMachine

class CoffeMachine(unittest.TestCase):

    def test1_NoCoin(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.coins,0)

    def test2_CountOfCoins(self):
        machine = CoffeeMachine(2)
        for insertsAmount in range(0,3): machine.insertCoin()
        self.assertEqual(machine.coins,5)

    def test3_CoffeePetitionNoCoins(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.giveCoffee(0),'Not enough coins')
        self.assertEqual(machine.giveCoffee(1),'Not enough coins')

    def test4_CoffePetition(self):
        machine = CoffeeMachine()
        machine.insertCoin()
        self.assertEqual(machine.giveCoffee(0),'Give Black Coffee')
        self.assertEqual(machine.amountCoffee,125)
        machine.insertCoin()
        self.assertEqual(machine.giveCoffee(1),'Give Black Coffee With Sugar')
        self.assertEqual(machine.amountCoffee,100)

    def test5_ReturnCoinPetition(self):
        machine = CoffeeMachine()
        machine.insertCoin()
        self.assertEqual(machine.returnCoin(),'Give coin back')
        self.assertEqual(machine.coins,0)

    def test6_ReturnCoinPetitionWithoutCoin(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.returnCoin(),'No coins')
        self.assertEqual(machine.coins,0)

    def test7_CoffeePetitionsMoreThanCoins(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.giveCoffee(0),'Not enough coins')
        machine.insertCoin()
        self.assertEqual(machine.giveCoffee(1),'Give Black Coffee With Sugar')
        self.assertEqual(machine.giveCoffee(1),'Not enough coins')
        
    def test8_CoffePetitionMoreThanAmountOfCoffee(self):
        machine = CoffeeMachine()
        for insertsAmount in range(0,7): machine.insertCoin()
        for petitionsAmount in range(0,6): machine.giveCoffee(0)
        self.assertEqual(machine.giveCoffee(0),'No more coffee')
        self.assertEqual(machine.giveCoffee(1),'No more coffee')

if __name__=='__main__':
    unittest.main()