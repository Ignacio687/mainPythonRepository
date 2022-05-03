
from operator import truediv


class CoffeeMachine():
    def __init__(self,coins,coffee,sugarCoffee,amountCoffe = 450):
        self.coins = coins
        self.coffee = coffee
        self.sugarCoffee = sugarCoffee
    def coins(self):
        if self.coins >=1:
            return True
        else: return False
    def give(self):
        operations = {}
        if self.coins > 1 and self.coffee >