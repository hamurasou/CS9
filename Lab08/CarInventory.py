# CarInventory.py

from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:

    def __init__(self):
        self.root = None

    """"""

    def addCar(self, car):
        # Consider 4 cases
        # 1. node doesn't exist in the BST
        # 2. node with the same make & model exists
        # 3. node will be inserted in the left subtree
        # 4. node will be inserted in the right subtree

        # 1. node doesn't exist in the BST
        if self.root is None: 
            self.root = CarInventoryNode(car)
        # case 2, 3, 4: recursively go down the tree to find the correct location
        else:
            self._addCarRecursively(self.root, car)

    def _addCarRecursively(self, current_node, car):
        
        # 2. node with the same make & model exists
        if car.make == current_node.make and car.model == current_node.model:
            current_node.cars.append(car)

        else: 
            # 3. node will be inserted in the left subtree
            if car < current_node.cars[0]: # Use the first car in the node to compare

                # left child doesn't exist
                if current_node.left is None:
                    new_node = CarInventoryNode(car)
                    current_node.left = new_node
                    new_node.parent = current_node
                
                # left child exists -> recall the fucntion with the left child (go down the tree)
                else:
                    left_child = current_node.left
                    self._addCarRecursively(left_child, car)
            
            # 4. node will be inserted in the right subtree
            elif car > current_node.cars[0]: # Use the first car in the node to compare
                
                # right child doesn't exist
                if current_node.right is None:
                    new_node = CarInventoryNode(car)
                    current_node.right = new_node
                    new_node.parent = current_node
                
                # right child exists -> recall the function with the right child (go down the tree)
                else:
                    right_child = current_node.right
                    self._addCarRecursively(right_child, car)


    """"""

    def doesCarExist(self, car):
        found_node = self._findNodeRecursively(self.root, car)
        if found_node is not None:
            return car in found_node.cars # True if car is in the list / False if it isn't
        else:
            return False
    
    def _findNodeRecursively(self, current_node, car):

        # Base case: it reaches the bottom of the tree
        if current_node is None: 
            return None
        
        # the node with the same make and model exists
        if car.make == current_node.make and car.model == current_node.model:
            return current_node 
        
        # recursively search the left subtree
        elif car < current_node: 
            return self._findNodeRecursively(current_node.left, car)
        
        # recursively search the right subtree
        else: 
            return self._findNodeRecursively(current_node.right, car)


    """"""

    def inOrder(self):
        return self._inOrderRecursively(self.root)
    
    def _inOrderRecursively(self, current_node):
        result = ""
        if current_node is None:
            return result
        result += self._inOrderRecursively(current_node.getLeft())
        for car in current_node.cars:
            result += str(car) + "\n"
        result += self._inOrderRecursively(current_node.getRight())
        return result
                

    """"""

    def preOrder(self):
        return self._preOrderRecursively(self.root)
    
    def _preOrderRecursively(self, current_node):
        result = ""
        if current_node is None:
            return result
        for car in current_node.cars:
            result += str(car) + "\n"
        result += self._preOrderRecursively(current_node.getLeft())
        result += self._preOrderRecursively(current_node.getRight())
        return result


    """"""

    def postOrder(self):
        return self._postOrderRecursively(self.root)
    
    def _postOrderRecursively(self, current_node):
        result = ""
        if current_node is None:
            return result
        result += self._postOrderRecursively(current_node.getLeft())
        result += self._postOrderRecursively(current_node.getRight())
        for car in current_node.cars:
            result += str(car) + "\n"
        return result


    """"""

    def getBestCar(self, make, model):

        found_node = self._findMakeModelRecursively(self.root, make, model)

        if found_node is None:
            return None
        
        else:
            car_list = found_node.cars
            current_best_car = None

            for car in car_list:
                if current_best_car is None:
                    current_best_car = car
                elif car.year > current_best_car.year:
                    current_best_car = car
                elif (car.year == current_best_car.year) and (car.price > current_best_car.price):
                    current_best_car = car

            return current_best_car


    def getWorstCar(self, make, model):

        found_node = self._findMakeModelRecursively(self.root, make, model)

        if found_node is None:
            return None
        
        else:
            car_list = found_node.cars
            current_worst_car = None

            for car in car_list:
                if current_worst_car is None:
                    current_worst_car = car
                elif car.year < current_worst_car.year:
                    current_worst_car = car
                elif (car.year == current_worst_car.year) and (car.price < current_worst_car.price):
                    current_worst_car = car

            return current_worst_car


    def _findMakeModelRecursively(self, current_node, make, model):

        # Base case: it reaches the edge of the tree
        if current_node is None: 
            return None
        
        # there is a node that matches the car's make and model
        if current_node.make == make.upper() and current_node.model == model.upper():
            return current_node 
        
        # recursively search the left subtree
        elif make.upper() < current_node.make or (make.upper() == current_node.make and model.upper() < current_node.model): 
            return self._findMakeModelRecursively(current_node.left, make, model)
        
        # recursively search the right subtree
        else: 
            return self._findMakeModelRecursively(current_node.right, make, model)


    """"""

    def getTotalInventoryPrice(self):

        if self.root is None:
            return 0.0
        
        else:
            car_list = self._getAllCarsRecursively(self.root)
            total_price = 0

            for car in car_list:
                total_price += car.price

            return total_price

    def _getAllCarsRecursively(self, current_node):
        car_node_list = []

        if current_node is None:
            return car_node_list
        
        else:
            car_node_list += current_node.cars
            car_node_list += self._getAllCarsRecursively(current_node.left)
            car_node_list += self._getAllCarsRecursively(current_node.right)
            return car_node_list

""""""
