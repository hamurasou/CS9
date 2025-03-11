# SpecialtyPizza.py

from Pizza import Pizza

class SpecialtyPizza(Pizza):

    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
    
        if size == "S":
            self.setPrice(12.00)
        elif size == "M":
            self.setPrice(14.00)
        elif size == "L":
            self.setPrice(16.00)
    
    def getPizzaDetails(self):
        pizza_details = ""
        pizza_details += "SPECIALTY PIZZA\n"
        pizza_details += f"Size: {self.size}\n"
        pizza_details += f"Name: {self.name}\n"
        pizza_details += f"Price: ${self.getPrice():.2f}\n"
        return pizza_details
