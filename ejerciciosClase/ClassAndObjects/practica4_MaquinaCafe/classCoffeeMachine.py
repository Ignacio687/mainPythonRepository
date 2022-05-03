
from operator import truediv


class CoffeeMachine():
    def __init__(self,coins = 0,coffee = 0,sugarCoffee = 0,amountCoffee = 150):
        self.coins = coins
        self.coffee = coffee
        self.sugarCoffee = sugarCoffee
        self.amountCoffee = amountCoffee
    def insertCoin(self,coins):
        self.coins =+ coins
    def giveCoffee(self,):
        
