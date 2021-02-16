# Lab 7
# Author: Adnan Fahad Faizi
# Email: adnan500@my.yorku.ca
# Student ID: 217905928

import pytest
from typing import List

# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:   # given
    myList.sort()

def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()

def getMinMax(myList: List[int], minormax: str) -> int:   # given -- but requires additional assert
    assert minormax.upper() == "MAX" or minormax.upper() == "MIN", "2nd argument must be 'Min' or 'Max' "
    lengthMylist = len(myList)
    assert lengthMylist != 0, "Error! the list can't be empty"
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result

# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()


#####
# WRITE YOUR TEST CASES BELOW HERE
#
######

def test_getMinMaxCase1():
    twoItem = [4, 2]
    initializeMinMaxList(twoItem)
    min = getMinMax(twoItem, "MIN")
    assert min == 2, "Min should be 2"
    max = getMinMax(twoItem, "MAX")
    assert max == 4, "Max should be 4"

def test_getMinMaxCase2():
    singleList = [10]
    initializeMinMaxList(singleList)
    min = getMinMax(singleList, "MIN")
    assert min == 10, "Min should be 10"
    insertItem(singleList, 10)
    max = getMinMax(singleList, "MAX")
    assert max == 10, "Max should be 10"

def test_getMinMaxCase3():
    emptyList = []
    initializeMinMaxList(emptyList)
    insertItem(emptyList, 8)
    insertItem(emptyList, 11)
    min = getMinMax(emptyList, "MIN")
    assert min == 8, "Min should be 8"
    max = getMinMax(emptyList, "MAX")
    assert max == 11, "Max should be 11"

def test_getMinMaxRequestError():
    threeItem = [7, 8, 9]
    with pytest.raises(AssertionError) as e:
        getMinMax(threeItem, "MID")
    assert e.typename == "AssertionError", "Should raise AssertionError!"

def test_getMinMaxEmptyError():
    emptyList = []
    initializeMinMaxList(emptyList)
    with pytest.raises(AssertionError) as e:
        getMinMax(emptyList, "MIN")
    assert e.typename == "AssertionError", "Should raise AssertionError!"
