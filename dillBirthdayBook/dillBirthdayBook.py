def loadData(fileSpec):
    txtReader = open(fileSpec, 'r')
    birthdays = {}
    for line in txtReader:
        birthdays[line.split(",")[0] +", " +line.split(",")[1]] = line.split(",")[2]

    return birthdays


def saveData(fileSpec, dictionary):
    txtWriter = open(fileSpec, "w")
    for people in dictionary:
        txtWriter.write(people.split(", ")[0] +"," +people.split(", ")[1] +"," +dictionary.get(people))


def addPerson(dictionary):
    print("")
    fName = input("Enter first name: ")
    lName = input("Enter last name: ")
    bd = addBirthday()
    dictionary.update({lName +", " +fName: bd})
    return dictionary


def displayAll(dictionary):
    print("")
    for people in sorted(dictionary.items()):
        print(people)

    print("\nAll birthdays shown above")


def addBirthday():
    print("Enter birthday in form of mm/dd/yyyy")
    month = input("Enter month of birth: ")
    while len(month) != 2:
        print("Invalid length")
        month = input("Enter month of birth: ")

    day = input("Enter day of birth: ")
    while len(day) != 2:
        print("Invalid length")
        day = input("Enter day of birth: ")

    year = input("Enter year of birth: ")
    while len(year) != 4: #makes user re-enter year until it is 4 characters long
        print("Invalid length")
        year = input("Enter year of birth: ")

    return month +"/" +day +"/" +year


def editPerson(lastName, firstName, dictionary):
    if dictionary.get(lastName +", " +firstName) == None: #returns dictionary uneditted if the person is not found
        print("That person was not found")
        return dictionary

    dictionary[lastName +", " +firstName] = addBirthday()
    return dictionary


def delPerson(lastName, firstName, dictionary):
    if dictionary.get(lastName +", " +firstName) == None:
        print("That person does not exist")
        return dictionary

    if input("Are you sure you want to delete " +firstName +" " +lastName +" (y/n): ") =="n":
        return dictionary

    dictionary.pop(lastName +", " +firstName)

    return dictionary


def quit(dictionary):
    print("Good bye")
    saveData("bDayData.txt", dictionary)


def menu(birthdays):
    option = 0
    while option != 5:
        option = int(input("\nOptions\n1. Add Person\n2. Display People\n3. Edit Person\n4. Delete Person\n5. Quit\nWhat would you like to do: "))
        if option == 1:
            birthdays = addPerson(birthdays)
        elif option == 2:
            displayAll(birthdays)
        elif option == 3:
            birthdays = editPerson(input("Enter last name: "), input("Enter first name: "), birthdays)
        elif option == 4:
            birthdays = delPerson(input("Enter last name: "), input("Enter first name: "), birthdays)
        elif option == 5:
            quit(birthdays)


def main():
    print("Welcome to the birthday book!")
    menu(loadData("bDayData.txt"))
main()