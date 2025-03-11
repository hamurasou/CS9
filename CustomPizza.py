# CustomPizza.py

from Pizza import Pizza

class CustomPizza(Pizza):

    def __init__(self, size):
        super().__init__(size)
        self.toppings = []

        if size == "S":
            self.setPrice(8.00)
        elif size == "M":
            self.setPrice(10.00)
        elif size == "L":
            self.setPrice(12.00)

    def addTopping(self, topping):
        self.toppings.append(topping)
        original_price = self.getPrice()
        if self.getSize() == "S":
            self.setPrice(original_price + 0.50)
        elif self.getSize() == "M":
            self.setPrice(original_price + 0.75)
        elif self.getSize() == "L":
            self.setPrice(original_price + 1.00)
    
    def getPizzaDetails(self):
        pizza_details = ""
        pizza_details += "CUSTOM PIZZA\n"
        pizza_details += f"Size: {self.getSize()}\n"
        pizza_details += "Toppings:\n"
        for topping in self.toppings:
            pizza_details += f"\t+ {topping}\n"
        pizza_details += f"Price: ${self.getPrice():.2f}\n"
        return pizza_details





