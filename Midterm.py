#TASK 0
def task0():
    print("Midterm Exam - EECS1015\nNAME: ADNAN FAHAD FAIZI\nStudent ID: 217905928\nemail: adnan500@my.yorku.ca")

#TASK 1
def task1():
    firstName = input("Your first name: ").strip().capitalize()
    lastName = input("Your last name: ").strip().upper()
    weeklyHours = float(input("Hours you work per week: "))
    hourlyWage = float(input("Hourly wage: "))
    monthlySalary = weeklyHours * hourlyWage * 4
    taxDeduction = monthlySalary * 0.25
    monthlySalaryNet = monthlySalary - taxDeduction
    print(f"Employee:{lastName}, {firstName} ")
    print(f"${monthlySalary:.2f} Monthly salary (gross) ")
    print(f"$-{taxDeduction:.2f} 25% Tax deduction")
    print(f"${monthlySalaryNet:.2f} Monthly salary (net)")

#TASK 2

def task2():
    initialBalance = 10.00
    falafelP = 3.00
    pizzaP = 6.00
    saladP = 1.50
    coffeeP = 1.00
    ordering = True
    while ordering:
        print(f"You have ${initialBalance:.2f} - what item do you want?")
        print("1: Falafel $3.00\n2: Pizza $6.00\n3: Salad $1.50\n4: Coffee: $1.00")
        print("Enter 0 to exit.")
        if ((initialBalance < pizzaP) and (initialBalance < saladP) and (initialBalance < coffeeP) and (
                initialBalance < falafelP)) and (
                initialBalance > 0):  # doesn't show the data if we have a balance of 0.50
            print("sorry, you don't have enough money to buy any item")
            ordering = False
        yourOrder = int(input("Your order: "))
        if yourOrder == 1:
            if initialBalance >= 3.00:
                initialBalance = initialBalance - 3.00
                print("order for *falafel* confirmed")
            else:
                print("Sorry, you don't have enough money for that item.")
        elif yourOrder == 2:
            if initialBalance >= 6.00:
                initialBalance = initialBalance - 6.00
                print("order for *pizza* confirmed")
            else:
                print("Sorry, you don't have enough money for that item.")
        elif yourOrder == 3:
            if initialBalance >= 1.50:
                initialBalance = initialBalance - 1.50
                print("order for *salad* confirmed")
            else:
                print("Sorry, you don't have enough money for that item.")
        elif yourOrder == 4:
            if initialBalance >= 1.00:
                initialBalance = initialBalance - 1.00
                print("order for *coffee* confirmed")
            else:
                print("Sorry, you don't have enough money for that item.")
        elif yourOrder == 0:
            ordering = False
            print("Thank you!")
        else:
            ordering = True
        if ((initialBalance < pizzaP) and (initialBalance < saladP) and (initialBalance < coffeeP) and (
                initialBalance < falafelP)) or initialBalance == 0:
            print("Thank you!")
            break

#TASK3
def task3():
    print("Rolling dice 10 times . . .")
    from random import randint
    play = True
    while play:
        x = 0
        for dice in range(1, 11):
            dice = randint(1, 6)
            if dice == 6:
                printWL = f"*[{dice}]*"
                print(printWL)
                x = x + 1
            elif dice != 6:
                print(f"[{dice}]")
        if x >= 2:
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
            play = False
        prompt = input("Do you want to play again? (Y/N)").upper()
        if prompt == "Y":
            play = True
        elif prompt == "N":
            play = False

#TASK4
from random import randint
replaceDna = randint(0, 39)
replaceindex = replaceDna

def task4():
    def generateDNASequence():
        from random import randint
        a = ""
        for x in range(1, 41):
            x = randint(1, 4)
            if x == 1:
                x = "T"
            elif x == 2:
                x = "G"
            elif x == 3:
                x = "C"
            elif x == 4:
                x = "A"
            a = a + x
        return a

    Function1 = generateDNASequence()

    def applyGammaRadiation(Function1):
        global replaceindex

        def randomDNA():
            from random import randint
            tgca = randint(1, 4)
            if tgca == 1:
                tgca = "T"
            elif tgca == 2:
                tgca = "G"
            elif tgca == 3:
                tgca = "C"
            elif tgca == 4:
                tgca = "A"
            return tgca

        dnastring = Function1
        from random import randint
        mutateOrNot = randint(1, 100)
        if mutateOrNot > 50:
            lockrandomDNA = randomDNA()  # s = s[:index] + newstring + s[index + 1:]
            if dnastring[replaceindex] != lockrandomDNA:
                newdnastring = dnastring[:replaceindex] + f"{lockrandomDNA}" + dnastring[replaceindex + 1:]
                return newdnastring
            elif dnastring[replaceindex] == lockrandomDNA:
                if dnastring[replaceindex] and lockrandomDNA == "A":
                    A = randint(1, 3)
                    lockA = A
                    if lockA == 1:
                        lockA = "G"
                    elif lockA == 2:
                        lockA = "T"
                    else:
                        lockA = "C"
                    newdnastring = dnastring[:replaceindex] + f"{lockA}" + dnastring[replaceindex + 1:]
                    return newdnastring
                elif dnastring[replaceindex] and lockrandomDNA == "G":
                    A = randint(1, 3)
                    lockA = A
                    if lockA == 1:
                        lockA = "A"
                    elif lockA == 2:
                        lockA = "T"
                    else:
                        lockA = "C"
                    newdnastring = dnastring[:replaceindex] + f"{lockA}" + dnastring[replaceindex + 1:]
                    return newdnastring
                elif dnastring[replaceindex] and lockrandomDNA == "C":
                    A = randint(1, 3)
                    lockA = A
                    if lockA == 1:
                        lockA = "G"
                    elif lockA == 2:
                        lockA = "T"
                    else:
                        lockA = "A"
                    newdnastring = dnastring[:replaceindex] + f"{lockA}" + dnastring[replaceindex + 1:]
                    return newdnastring
                elif dnastring[replaceindex] and lockrandomDNA == "T":
                    A = randint(1, 3)
                    lockA = A
                    if lockA == 1:
                        lockA = "G"
                    elif lockA == 2:
                        lockA = "A"
                    else:
                        lockA = "C"
                    newdnastring = dnastring[:replaceindex] + f"{lockA}" + dnastring[replaceindex + 1:]
                    return newdnastring
        else:
            return dnastring

    def detectMutation(unchangedDNA, changedDNA):
        global replaceindex
        print(unchangedDNA + " (DNA)")
        print(changedDNA + " (DNA after radiation)")
        if unchangedDNA[:] == changedDNA[:]:
            print(40 * "")
            print("NO MUTATION DETECTED")
        elif unchangedDNA != changedDNA:
            newChangedna = (replaceindex * " ") + "^" + ((replaceindex + 1) * " ")
            print(newChangedna)
            print("MUTATION DETECTED")
    detectMutation(Function1, applyGammaRadiation(Function1))


# EECS1015 - Midterm
# Name: Adnan Fahad Faizi
# Student ID: 217905928
# Email: adnan500@my.yorku.ca


# main function for EECS1015 midterm
def main():
    task0()
    print("\n-- TASK 1 --\n")
    task1()
    print("\n-- Task 2 --\n")
    task2()
    print("\n-- Task 3 --\n")
    task3()
    print("\n-- Task 4 --\n")
    task4()

if __name__=="__main__":
    main()


