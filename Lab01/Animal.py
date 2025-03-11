## Animal.py

class Animal:

    def __init__(self, species=None, weight=None, age=None, name=None):

        if isinstance(species, str):
            self.species = species.upper()
        else:
            self.species = None
        if isinstance(name, str):
            self.name = name.upper()
        else:
            self.name = None

        self.weight = weight
        self.age = age

    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        return f"Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

        
# OH Questions
'''
when the input is None the upper() function cannot be used and makes errors
how do i fix it
'''

# for init
# we can put if statement that filters the input and distingishes whether it's string
# if it's not a string the input just can be None

# if it's string, excute upper()
# else (it's None) do not excute upper() 



## input

# a = Animal("dog", 12.2, 2, "Ruffles")
# print(a.toString())

## output:

# Species: DOG, Name: RUFFLES, Age: 2, Weight: 12.2
