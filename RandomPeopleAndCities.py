# Lab 5
# Author: Adnan Fahad Faz\izi
# Email: adnan500@my.yorku.ca
# Student ID: 217905928

names = ("Masha", "Kevin", "Ruigang", "Vlad", "Ramesh", "Aditi", "Caroline", "Panos", "Chuck", "Grani", "Rutha", "Stan", "Qiong", "Alexi", "Carlos")
cities = ("Toronto", "Ottawa", "Hamilton")

testDict = {"Richard": "Toronto", "Jia-Tao": "Toronto", "Justin": "Ottawa", "Lars": "Ottawa"}

from random import randint
def getRandomItem(tupleOrList):  # Returns a random element of a list or tuple when given as an argument inside the function
    randomItemFromTuple = randint(0, len(tupleOrList) - 1)
    randomItem = tupleOrList[randomItemFromTuple]
    return randomItem

def createNameDictionary():
    global names, cities
    dictMixNamesToCities = {}
    for x in names:
        dictMixNamesToCities[x] = getRandomItem(cities)
    return dictMixNamesToCities


def fromCity(dectionary, stringCity):
    listNameCity = []
    for i in dectionary:
        if dectionary[i] == stringCity:
            listNameCity.append(i)
    return listNameCity

def removePeopleFrom(dictionary, string):
    list = []
    for x in dictionary:
        if dictionary[x] == string:
            list.append(x)
    for item in list:
        del dictionary[item]


def printNameDict(dictionary, tuple):
    if len(tuple) == 1:
        peopleCity = fromCity(dictionary, tuple[0])
        if len(peopleCity) == 0:
            print(f"People from {tuple[0]}:")
            print("*None*")
        elif len(peopleCity) > 0:
            print(f"People from {tuple[0]}:")
            for i in range(0, len(peopleCity)):
                print(f"{i+1}. {peopleCity[i]}")
        return ""


    elif len(tuple) == 2:
        peopleCity = fromCity(dictionary, tuple[0])
        if len(peopleCity) == 0:
            print(f"People from {tuple[0]}:")
            print("*None*")
        elif len(peopleCity) > 0:
            print(f"People from {tuple[0]}:")
            for i in range(0, len(peopleCity)):
                print(f"{i + 1}. {peopleCity[i]}")

        peopleCity1 = fromCity(dictionary, tuple[1])
        if len(peopleCity1) == 0:
            print(f"People from {tuple[1]}:")
            print("*None*")
        elif len(peopleCity1) > 0:
            print(f"People from {tuple[1]}:")
            for i in range(0, len(peopleCity1)):
                print(f"{i+1}. {peopleCity1[i]}")
        return ""

    elif len(tuple) == 3:
        peopleCity = fromCity(dictionary, tuple[0])
        if len(peopleCity) == 0:
            print(f"People from {tuple[0]}:")
            print("*None*")
        elif len(peopleCity) > 0:
            print(f"People from {tuple[0]}:")
            for i in range(0, len(peopleCity)):
                print(f"{i + 1}. {peopleCity[i]}")

        peopleCity1 = fromCity(dictionary, tuple[1])
        if len(peopleCity1) == 0:
            print(f"People from {tuple[1]}:")
            print("*None*")
        elif len(peopleCity1) > 0:
            print(f"People from {tuple[1]}:")
            for i in range(0, len(peopleCity1)):
                print(f"{i + 1}. {peopleCity1[i]}")

        peopleCity2 = fromCity(dictionary, tuple[2])
        if len(peopleCity2) == 0:
            print(f"People from {tuple[2]}:")
            print("*None*")
        elif len(peopleCity2) > 0:
            print(f"People from {tuple[2]}:")
            for i in range(0, len(peopleCity2)):
                print(f"{i + 1}. {peopleCity2[i]}")
        return ""


def main():
    # part 1 (Function testing)
    print("\nPart 1 - Testing functions with `testDict'\n")
    print("Testing getRandomItem() function")
    getRandom = getRandomItem(cities)
    print(cities)
    print(f"Items: {getRandom}")
    print("Testing fromCity() function")
    toronto = fromCity(testDict, "Toronto")
    print(toronto)
    ottawa = fromCity(testDict, "Ottawa")
    print(ottawa)
    print("Testing printNameDict() function")
    torontoOttawa = printNameDict(testDict, ("Toronto", "Ottawa",))
    print(torontoOttawa)
    print("Testing removePeopleFrom() function")
    removePeopleFrom(testDict, "Ottawa")
    removedForm = printNameDict(testDict, ("Toronto", "Ottawa",))
    print(removedForm)
    # part 2 (Main program with generated Dictionary)
    print("\nPart 2 - Main\n")
    newDict = createNameDictionary()
    printNewDict = printNameDict(newDict, cities)
    print(printNewDict)
    torontoNew = fromCity(newDict, "Toronto")
    print("Toronto List: ")
    print(torontoNew)
    ottawaNew = fromCity(newDict, "Ottawa")
    print("Ottawa List: ")
    print(ottawaNew)
    hamiltonNew = fromCity(newDict, "Hamilton")
    print("Hamilton List: ")
    print(hamiltonNew)
    print("Removing all people from Toronto\nRemoving all people from Hamilton")
    removePeopleFrom(newDict, "Toronto")
    removePeopleFrom(newDict, "Hamilton")
    removed = printNameDict(newDict, cities)
    print(removed)
    input()

main()