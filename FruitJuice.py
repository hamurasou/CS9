from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        Beverage.__init__(self, ounces, price)
        self.fruits = fruits

    def getInfo(self):
        names = "/".join(self.fruits)
        info = super().getInfo()
        return f"{names} Juice, {info}"
