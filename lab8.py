# Lab 8
# Author: Adnan Fahad Faizi
# Email: adnan500@my.yorku.ca
# Student ID: 217905928

from random import randint


class Bacteria:

    def __init__(self, chanceOfDividing, maxLifeSpan):
        self.maxLifeSpan = maxLifeSpan
        self.chanceOfDividing = chanceOfDividing
        self.lifeSpan = randint(1, self.maxLifeSpan)       # The life span is a random number between 1 and max life span and the max life span is the maximum allowable life span

    def live_a_day(self):
        randomNumber = randint(1, 100)
        if randomNumber < self.chanceOfDividing:
            newBacteria = Bacteria(self.chanceOfDividing, self.maxLifeSpan)
            self.lifeSpan = self.lifeSpan - 1         # this will decrease the life of the bacteria and make it to eventually die
            return newBacteria
        else:
            self.lifeSpan = self.lifeSpan - 1
            return None

    def is_alive(self):
        if self.lifeSpan > 0:         # and of course if lifespan is less than 0 it means the bacteria is no more alive and it should die down
            return True
        else:
            return False


class Colony:
    totalBacteria = 0
    day = 0

    def __init__(self, seed):
        self.seed = seed

    def live_a_day(self, printDailyReport=True):
        global numOfAllowedGrow, addDividableBacteria, addDeadBacterias, startingBacteria         # it will help to use these variables to be used inside this class method specially on the formated string in line 63!
        self.diviadableBacteria = []
        self.colonyDead = []           # these are instance lists that are only for that specific lists and are not used in for the whole bacteria
        self.printDailyReport = printDailyReport

        for eachElement in self.seed:
            newBacteria = eachElement.live_a_day()  # checking each bacteria in the seed list to see if it's dividable or not
            isAlive = eachElement.is_alive()

            if newBacteria is None:
                pass  # this pass will help to pass to the next bacteria in the list if it hasn't been divided
            else:
                self.diviadableBacteria.append(newBacteria)   # if it's dividable it will be added to the the instance list
                addDividableBacteria.append(newBacteria)   # this is basically for the formatted string in the line 63

            if not isAlive:
                self.colonyDead.append(eachElement)     # adding bacterias that are dead(lived their life spans) in the instance list
                addDeadBacterias.append(eachElement)    # this is for the purpose of line 63
                self.seed.remove(eachElement)           # removing bacterias that are dead from the seed list
        self.seed.extend(self.diviadableBacteria)       # adding these to lists to get the modified seed list

        Colony.day = Colony.day + 1
        print(f"Day {Colony.day}  Colony Size {len(self.seed):5d} New Members {len(self.diviadableBacteria):6d} Expired Members {len(self.colonyDead):6d}")

    def print_colony_status(self):
        if self.printDailyReport == True:
            totalNumOFBacteria = (len(addDividableBacteria) + startingBacteria)
            Colony.totalBacteria = Colony.totalBacteria + totalNumOFBacteria
            print(f"""Colony report at day: {numOfAllowedGrow}\nCurrent colony population: {len(self.seed)}\nTotal number of Bacteria: {totalNumOFBacteria}\nTotal deceased bacteria: {len(addDeadBacterias)}""")

    def get_colony_size(self):
        if self.printDailyReport == True:
            print(f"Total number of bacteria objects created so far: {Colony.totalBacteria}")


def main():
    global numOfAllowedGrow, startingBacteria, addDividableBacteria, addDeadBacterias, add
    a = None

    numOfAllowedGrow = int(input("Max num of days to let the colony grow: "))
    startingBacteria = int(input("Number of starting bacteria: "))
    chanceOfDailyDivision = int(input("% chance of daily division [1-100]: "))
    maxLifeSpanForaBacteria = int(input("Maximum lifespan for a bacteria (1 or greater): "))

    addDividableBacteria = []
    addDeadBacterias = []

    seed = []
    for i in range(startingBacteria):      # to create the initial seed list to be passed in the colony list, shown in the line 93
        seed.append(Bacteria(chanceOfDailyDivision, maxLifeSpanForaBacteria))

    for k in range(numOfAllowedGrow):
        a = Colony(seed)
        a.live_a_day()       # applying live a day method on each element in the seed list to check if it's dividable with the help of range(numOfAllowedGrow)
        if (len(seed) == 0) or (len(seed) >= 50000):
            print("Experiment Stopped")
            break

    a.print_colony_status()
    print("")
    a.get_colony_size()


if __name__ == '__main__':
    main()

tryAgain = input("try another experiment? (Y/N)").upper()
while tryAgain == "Y":
    Colony.day = 0                    # this is really important for the line 63, when the while loop is asked the user and the user inputs "Y" then for the second loop it will help the days to start from 1 again
    if __name__ == '__main__':
        main()
    tryAgain = input("try another experiment? (Y/N)").upper()
    if tryAgain == "N":
        break

