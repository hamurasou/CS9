# testFile.py

import pytest
from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

# Car.py

def test_car_class():

    car1 = Car("Honda", "Civic", 2015, 10000)
    assert car1.make == "HONDA"
    assert car1.model == "CIVIC"
    assert car1.year == 2015
    assert car1.price == 10000
    assert str(car1) == "Make: HONDA, Model: CIVIC, Year: 2015, Price: $10000"

    # > , < , ==

    car2 = Car("Toyota", "Camry", 2018, 15000)
    car3 = Car("Honda", "Civic", 2015, 9000)
    assert car2 > car1
    assert car3 < car1
    assert car1 == Car("Honda", "Civic", 2015, 10000)

# CarInventoryNode.py

def test_car_inventory_node_class():

    car1 = Car("Toyota", "Prius", 2018, 20000)
    car2 = Car("Toyota", "Prius", 2015, 15000)
    node = CarInventoryNode(car1)
    assert node.make == "TOYOTA"
    assert node.model == "PRIUS"
    assert node.cars[0] == car1

    node.cars.append(car2)
    assert len(node.cars) == 2
    assert node.cars[1] == car2
    assert str(node) == "Make: TOYOTA, Model: PRIUS, Year: 2018, Price: $20000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $15000\n"


# CarInventory.py

def test_car_inventory_class():

    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Honda", "Accord", 2020, 22000)

    # addCar()

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    # inOrder() / preOrder() / postOrder()
    
    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""

    # doesCarExist()

    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car6) == False

    # getBestCar()

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None
    

    # getWorkCar()

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getWorstCar("Honda", "Accord") == None

    # getTotalInventoryPrice()

    assert bst.getTotalInventoryPrice() == 158000


