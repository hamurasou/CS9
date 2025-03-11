# Apartment.py

class Apartment:

    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent
    
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    
    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return f"(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}"



# First, you will organize the Apartment by increasing rent.
# In the event of a tie (several Apartments have the same rent), 
# the meters from UCSB will be used to determine the Apartment’s place in the list. 
# The closer the apartment is to campus, the better. 
# If the rent and the meters from campus are the same, 
# then the Apartment’s condition will be used to determine the Apartment’s place in the list. 
# An apartment can have either a "bad", "average", or "excellent" condition 
# - the better the condition is, the better the apartment. 
# You may assume that apartment objects will have either 
# "bad", "average", or "excellent" as their condition when comparing / sorting apartments.


    def __lt__(self, rhs):
        if self.rent < rhs.rent:
            return True
        elif self.rent > rhs.rent:
            return False
        else:
            if self.metersFromUCSB < rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB > rhs.metersFromUCSB:
                return False
            else:
                condition_rank = {"bad": 1, "average": 2, "excellent": 3}
                return condition_rank[self.condition] > condition_rank[rhs.condition]

    def __gt__(self, rhs):
        if self.rent > rhs.rent:
            return True
        elif self.rent < rhs.rent:
            return False
        else:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB < rhs.metersFromUCSB:
                return False
            else:
                condition_rank = {"bad": 1, "average": 2, "excellent": 3}
                return condition_rank[self.condition] < condition_rank[rhs.condition]

    
    def __eq__(self, rhs):
        if (self.rent == rhs.rent and
            self.metersFromUCSB == rhs.metersFromUCSB and
            self.condition == rhs.condition):
            return True
        else:
            return False
    