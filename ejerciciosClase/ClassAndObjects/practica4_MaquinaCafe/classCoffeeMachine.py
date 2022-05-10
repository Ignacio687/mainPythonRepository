
from operator import truediv


class CoffeeMachine():
    def __init__(self,coins = 0,coffee = 0,sugarCoffee = 0,amountCoffee = 150):
        self.coins = coins
        self.coffee = coffee
        self.sugarCoffee = sugarCoffee
        self.amountCoffee = amountCoffee
    def insertCoin(self):
        self.coins +=1
    def giveCoffee(self, tipe):
        if self.amountCoffee >= 25:
            self.amountCoffee -=25
            if self.coins > 0:
                self.coins -=1
                if tipe == 0:
                    return 'Give Black Coffee'
                else: return 'Give Black Coffee With Sugar'
            else: return 'Not enough coins'
        else: return 'No more coffee'
    def returnCoin(self):
        if self.coins >0:
            self.coins -=1
            return 'Give coin back'
        else: return 'No coins'
