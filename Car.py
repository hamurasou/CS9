# Car.py

class Car:

    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        # Compare "make"
        if self.make > rhs.make:
            return True
        elif self.make < rhs.make:
            return False
        # Compare "model"
        if self.model > rhs.model:
            return True
        elif self.model < rhs.model:
            return False
        # Compare "year" from least to greatest
        if self.year > rhs.year:
            return True
        elif self.year < rhs.year:
            return False
        # Compare "price" from least to greatest
        return self.price > rhs.price

    def __lt__(self, rhs):
        # Compare "make"
        if self.make < rhs.make:
            return True
        elif self.make > rhs.make:
            return False
        # Compare "model"
        if self.model < rhs.model:
            return True
        elif self.model > rhs.model:
            return False
        # Compare "year"
        if self.year < rhs.year:
            return True
        elif self.year > rhs.year:
            return False
        # Compare "price"
        return self.price < rhs.price

    def __eq__(self, rhs):
        return (self.make == rhs.make and
                self.model == rhs.model and
                self.year == rhs.year and
                self.price == rhs.price)
    
    def __str__(self):
        return f"Make: {self.make.upper()}, Model: {self.model.upper()}, Year: {self.year}, Price: ${self.price}"