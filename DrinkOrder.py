class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        total = sum(drink.getPrice() for drink in self.drinks)
        if not self.drinks:
            return "Order Items:\nTotal Price: $0.00"
        detail = "\n".join(f"* {drink.getInfo()}" for drink in self.drinks)
        return f"Order Items:\n{detail}\nTotal Price: ${total:.2f}"
