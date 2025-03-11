# lab06.py

from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0 # index for lefthalf sublist
        j = 0 # index for righthalf sublist
        k = 0 # index for apartmentList
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i = i + 1
            else:
                 apartmentList[k] = righthalf[j]
                 j = j + 1
            k = k + 1
        
        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        
        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1


def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList) - 1):
        if apartmentList[i] > apartmentList[i + 1]:
            return False
    return True


def getBestApartment(apartmentList):
    mergesort(apartmentList)

    best_apartment = apartmentList[0]
    return best_apartment.getApartmentDetails()


def getWorstApartment(apartmentList):
    mergesort(apartmentList)

    worst_apartment = apartmentList[-1]
    return worst_apartment.getApartmentDetails()


def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)

    affordable_apartments = []
    for apartment in apartmentList:
        if apartment.getRent() <= budget:
            affordable_apartments.append(apartment)

    if not affordable_apartments:
        return ""
    
    details_list = []
    for apartment in affordable_apartments:
        details_list.append(apartment.getApartmentDetails())
        
    affordable_details = "\n".join(details_list)

    return affordable_details

