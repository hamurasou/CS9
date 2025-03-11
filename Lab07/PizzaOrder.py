# PizzaOrder.py

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder():
    def __init__(self, time):
        self.time = time
        self.pizzas = []

    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        total_price = 0.0

        description = ""
        description += "******\n"
        description += f"Order Time: {self.getTime()}\n"
        for pizza in self.pizzas:
            description += pizza.getPizzaDetails()
            description += "\n"
            description += "----\n"

            total_price += pizza.getPrice()

        description += f"TOTAL ORDER PRICE: ${total_price:.2f}\n"
        description += "******\n"
        return description

