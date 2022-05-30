class CoffeeMachinePlus:
    def __init__(self):
        self.resources = {
            'sugar': 0,
            'coffee': 0,
            'tea': 0,
        }
        self.recipies = {
            'coffee_alone': {
                'coffe': 30,
            },
            'coffee_double': {
                'coffe': 60,
            },
            'tea_simple': {
                'tea': 10,
            },
        }

    def add_resource(self, type, amount):
        self.resources[type] += amount