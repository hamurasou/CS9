# OrderQueue.py

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder


class QueueEmptyException(Exception):
    # it gets raised when the queue list is empty
    pass


class OrderQueue:
    def __init__(self):
        self.orderQueue = MinHeap()
    
    def addOrder(self, pizzaOrder):
        orderTime = pizzaOrder.getTime()
        self.orderQueue.insert(pizzaOrder)

    def processNextOrder(self):
        if self.orderQueue.currentSize == 0:
            raise QueueEmptyException()

        nextOrder = self.orderQueue.delMin()
        return nextOrder.getOrderDescription()

class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].getTime() < self.heapList[i // 2].getTime():
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            min_child = self.minChild(i)
            if self.heapList[i].getTime() > self.heapList[min_child].getTime():
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[min_child]
                self.heapList[min_child] = tmp
            i = min_child
    
    def minChild(self, i):
        if (i * 2 + 1) > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2].getTime() < self.heapList[i * 2 + 1].getTime():
                return i * 2
            else: 
                return i * 2 + 1
            
    def delMin(self):
        min_value = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return min_value


