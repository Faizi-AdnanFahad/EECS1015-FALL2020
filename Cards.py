# Lab 4
# Author: Adnan Fahad Faizi
# Email: adnan500@my.yorku.ca
# Student ID: 217905928


from random import randint

def drawcards():
    firstcard = randint(2, 14)
    secondcard = randint(2, 14)
    if firstcard >= secondcard:
        return firstcard, secondcard
    else:
        return secondcard, firstcard

def card2str(changetostring):
    strchangetostring = str(changetostring)
    if changetostring == 11:
        strchangetostring = "J"
    elif changetostring == 12:
        strchangetostring = "Q"
    elif changetostring == 13:
        strchangetostring = "K"
    elif changetostring == 14:
        strchangetostring = "A"
    return strchangetostring


def printhand(card1, card2, playerName):
    print(f"[{card1}] [{card2}] {playerName}")


def printoutcome(die1User, die2User, die1Pc, die2Pc):
    if (die1User == die2User) and (die1Pc == die2Pc):
        if (die1User or die2User) > (die1Pc or die2Pc):
            print("YOU WIN")
        elif (die1User or die2User) < (die1Pc or die2Pc):
            print("YOU LOSE")
        else:
            print("TIE!")

    if (die1Pc == die2Pc) and (die1User != die2User):
        print("YOU LOSE")
    elif (die1User == die2User) and (die1Pc != die2Pc):
        print("YOU WIN")
    elif (die1User != die2User) and (die1Pc != die2Pc):
        if die1Pc > die1User:
            print("YOU LOSE")
        elif die1User > die1Pc:
            print("YOU WIN")
        elif die1User == die1Pc:
            if die2Pc > die2User:
                print("YOU LOSE")
            elif die2User > die2Pc:
                print("YOU WIN")
            else:
                print("TIE")

print("** EECS1015 -- AMAZING TWO CARD POKER GAME **")
keepPlaying = True
while keepPlaying:
    die1Pc, die2Pc = drawcards()
    die1PcStr = card2str(die1Pc)
    die2PcStr = card2str(die2Pc)
    pcName = "COMPUTER'S CARD"
    printhand(die1PcStr, die2PcStr, pcName)

    die1User, die2User = drawcards()
    die1UserStr = card2str(die1User)
    die2UserStr = card2str(die2User)
    userName = "YOUR CARDS"
    printhand(die1UserStr, die2UserStr, userName)

    printoutcome(die1User, die2User, die1Pc, die2Pc)

    playAgain = input("Do you want to play again(Y/N)?").upper()
    if playAgain == "Y":
        keepPlaying = True
    elif playAgain == "N":
        keepPlaying = False
        print("** Thanks for playing! **")
    else:
        keepPlaying = True


x = card