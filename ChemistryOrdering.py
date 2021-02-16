# Lab 6
# Author: Adnan Fahad Faizi
# Email: adnan500@my.yorku.ca
# Student ID: 217905928

# data for Task1
rList = [[1, 10, 9, 4, 50],
         [3, 40, 99, 37, 5, 1],
         [8, 11, 10, 94],
         [100, 9, 2, 88, 44],
         [4, 9, 2, 19]]

def printRaggedList(list):
    i = 0
    for sublist in list:
        print(f"Row {i}:  {sublist} ")
        i = i + 1

def sortRaggedList(list):
    for i in range(0, len(list)):
        list[i].sort()

# data for Task 2
encodedData1 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')], [(9, ' '), (3, '8'), (1, 'l')], [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')], [(6, ' '), (1, '.'), (8, '8'), (1, '.')], [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')], [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')], [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')], [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')], [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'), (1, "'")], [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'), (1, '-'), (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '), (1, 'm'), (1, 'h')]]
encodedData2 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')], [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')], [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'), (3, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'), (7, '.'), (7, ' '), (3, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'), (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'), (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'), (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')], [(52, '.')]]

def decodeTupleList(listOfTuples):
    i = ""
    for firstCharac in listOfTuples:
        string = firstCharac[0] * firstCharac[1]
        i = i + string
    return i

def printEncodedAsciiImage(list):
    for items in list:
        a = decodeTupleList(items)
        print(a)

# data for Task 3
stringData = "1 H Hydrogen,2 He Helium,3 Li Lithium,4 Be Beryllium,5 B Boron,6 C Carbon,7 N Nitrogen,8 O Oxygen,9 F Fluorine,10 Ne Neon,11 Na Sodium,12 Mg Magnesium,13 Al Aluminum,14 Si Silicon,15 P Phosphorus,16 S Sulfur,17 Cl Chlorine,18 Ar Argon,19 K Potassium,20 Ca Calcium,21 Sc Scandium,22 Ti Titanium,23 V Vanadium,24 Cr Chromium,25 Mn Manganese"

def buildElementDictionary(string):
    dictionarty = {}
    detailedList = string.split(",")
    for items in detailedList:
        listSplit = items.split()
        dictionarty[listSplit[1]] = [listSplit[2], listSplit[0]]
    return dictionarty

def printElements(dictionary):
    for keys in dictionary.keys():
        print(f"{keys} [{dictionary[keys][0]}] #{dictionary[keys][1]} ")


def main():
    print("Task 1 - Sorting and printing a ragged list")
    print("--List before sorting--")
    printRaggedList(rList)
    print("--List after sorting--")
    sortRaggedList(rList)
    printRaggedList(rList)
    print("\nTask 2 - Decoding Ascii Art")
    printEncodedAsciiImage(encodedData1)
    printEncodedAsciiImage(encodedData2)
    print("\nTask 3 - Elements String to Dictionary")
    n = buildElementDictionary(stringData)
    print(n)
    print("---First 25 Elements---")
    printElements(n)
    input()

main()