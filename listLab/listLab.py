def main(): #I tried to create all fucntions so that they would still work with an array of any size and even if the arrays are different sizes
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    list2 = ['one','two','three','four','five','six','Seven','Eight','nine','ten']
    print(makeCopy(list1))
    print(makeAnotherCopy(list2))
    print(calculateAverage(list1))
    findMinimum(list1)
    print(combineLists(list1, list2))
    print(reverseOrder(list1))
    print(removeItem(list1, 5))


def makeCopy(list):
    newList = []

    for contents in list:
        newList.append(contents)

    return newList


def makeAnotherCopy(list):
    newList = []

    while len(newList) != len(list):
        newList.append(list[len(newList)])

    return newList


def calculateAverage(list):
    average = 0

    for contents in list:
        average+=contents

    average/=len(list)
    return average


def findMinimum(list):
    min = list[0]

    for contents in list:
        if contents < min:
            min = contents

    print("Minimum value is", min, "found at index", list.index(min))

def combineLists(list1, list2):
    newList = []

    for contents in range(0, len(list1)):
        newList.append(list1[contents])
        newList.append(list2[contents])


    return newList


def reverseOrder(list):
    newList = [None] * len(list)

    for content in range(len(list) - 1, -1, -1):
        newList[len(list) - content - 1] = list[content]

    return newList

def removeItem(list, index):
    newList = [None] * (len(list) - 1)
    i = 0

    for content in range(0, len(list)):
        if content != index:
            newList[i] = list[content]
            i+=1
    return newList

main()
