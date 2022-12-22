import os

player = []
computer = []
choices = [1,2,3,4,5,6,7,8,9]
allChoices = [1,2,3,4,5,6,7,8,9]
winner = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
sign = ['X']

def printcross():
    for i in allChoices:
        if i in player:
            print('X', end='\t')
        elif i in computer:
            print('O', end='\t')
        else:
            print(i, end = '\t')
        if i % 3 == 0:
            print('\n\n')

def printChoices():
    print('Remain choices:')
    for i in choices:
        if not i in ('X','O'):
            print(i,end='\t')

def dogame():
    while True:
        printChoices()
        inputNumber = input('\nEnter your Choice: ')
        if inputNumber.isnumeric():
            inputNumber = int(inputNumber)
            if inputNumber in choices:
                if sign[0] == 'X':
                    player.append(inputNumber)
                    choices[inputNumber-1] = sign[0]
                    sign[0] = 'O'
                else:
                    computer.append(inputNumber)
                    choices[inputNumber-1] = sign[0]
                    sign[0] = 'X'
                break
        print('Wrong choice!\nTry again...')

def sub_lists (l):
    lists = [[]]
    for i in range(len(l)+1):
        for j in range(i):
            if len(l[j:i]) == 3:
                lists.append(l[j:i])
    return lists

def checkWin(l):
    for i in winner:
        for j in l:
            if sorted(j) == sorted(i):
                return True
    return False

while True:
    os.system('cls')
    print ('Welcome to Tic-Tac-Toe game...\n')
    printcross()
    dogame()
    if checkWin(sub_lists(player)) is True:
        os.system('cls')
        printcross()
        print('You win...')
        break
    elif checkWin(sub_lists(computer)) is True:
        os.system('cls')
        printcross()
        print('Computer win...')
        break
    else:
        checkList = []
        for i in choices:
            if not i in ('X', 'O'):
                checkList.append(i)
        if len(checkList) < 1:
            os.system('cls')
            printcross()
            print("It's tie...")
            break
