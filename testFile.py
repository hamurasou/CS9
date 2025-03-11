import pytest
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_beverage():
    bev = Beverage(16, 2.50)
    assert bev.getOunces() == 16
    assert bev.getPrice() == 2.50
    assert bev.getInfo() == "16 oz, $2.50"

def test_coffee():
    coffee = Coffee(8, 3.00, "Espresso")
    assert coffee.getOunces() == 8
    assert coffee.getPrice() == 3.00
    assert coffee.getInfo() == "Espresso Coffee, 8 oz, $3.00"

def test_fruitjuice():
    juice = FruitJuice(16, 4.50, ["Apple", "Guava"])
    assert juice.getOunces() == 16
    assert juice.getPrice() == 4.50
    assert juice.getInfo() == "Apple/Guava Juice, 16 oz, $4.50"

def test_drinkorder():
    order = DrinkOrder()
    coffee = Coffee(8, 3.00, "Espresso")
    juice = FruitJuice(16, 4.50, ["Apple", "Guava"])
    order.addBeverage(coffee)
    order.addBeverage(juice)
    assert order.getTotalOrder() == "Order Items:\nEspresso Coffee, 8 oz, $3.00\nApple/Guava Juice, 16 oz, $4.50\nTotal Price: $7.50"

if __name__ == "__main__":
    pytest.main()