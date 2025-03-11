from Beverage import Beverage

class Coffee(Beverage):
    def __init__(self, ounces, price, style):
        Beverage.__init__(self, ounces, price)
        self.style = style

    def getInfo(self):
        info = super().getInfo()
        return f"{self.style} Coffee, {info}"
