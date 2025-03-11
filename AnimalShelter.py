## AnimalShelter.py

class AnimalShelter:

    def __init__(self):

        self.shelter = {}
        # KEYS will be a str type representing an Animal’s species
        # all upper-case characters
        # VALUES will be a list of Animal objects that the AnimalShelter contains.

    def addAnimal(self, animal):
        if isinstance(animal.species, str):
            specie = animal.species.upper()
        else:
            specie = None
        if specie not in self.shelter:
            self.shelter[specie] = []
        self.shelter[specie].append(animal)

    def removeAnimal(self, animal):
        if isinstance(animal.species, str):
            specie = animal.species.upper()
        else:
            specie = None
        name = animal.name
        weight = animal.weight
        age = animal.age
        if specie in self.shelter:
            for each in range(len(self.shelter[specie])):
                check_animal = self.shelter[specie][each]
                if (check_animal.name == name and
                    check_animal.age == age and
                    check_animal.weight == weight):
                    del self.shelter[specie][each]
                    break
        
    def removeSpecies(self, species):
        if isinstance(species, str):
            specie = species.upper()
        else:
            specie = None
        if specie in self.shelter:
            del self.shelter[specie]

    def getAnimalsBySpecies(self, species):
        if isinstance(species, str):
            specie = species.upper()
        else:
            specie = None
        animal_list = self.shelter.get(specie)
        if specie in self.shelter:
            result = ""
            for animal in animal_list:
                result += animal.toString() + "\n"
            result = result[:-1]
            return result
        else:
            return ""

    def doesAnimalExist(self, animal):
        if isinstance(animal.species, str):
            specie = animal.species.upper()
        else:
            specie = None
        name = animal.name
        weight = animal.weight
        age = animal.age
        if specie in self.shelter:
            for check_animal in self.shelter[specie]:
                if (check_animal.name == name and
                    check_animal.age == age and
                    check_animal.weight == weight):
                    return True
            return False
        return False
        

# OH Questions

'''
when the input is None the upper() function cannot be used and makes errors
how do i fix it
according to the autograder, there is the same problem as class animal

did i even interpret the question right

did i even do it right
'''
'''
for getAnimalsBySpecies,
# create "" and add animals to it and put \n at the end
# sth  = sth[:-1]
'''

