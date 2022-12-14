player = []
computer = []
choices = [1,2,3,4,5,6,7,8,9]
allChoices = [1,2,3,4,5,6,7,8,9]
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

def dogame():
    while True:
        print('Remain choices:', choices)
        inputNumber = input('Enter your Choice: ')
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

print ('Welcome to Tic-Tac-Toe game...\n')
printcross()
print('*'*10,'\n',sign,'\n','*'*10)
dogame()
print('*'*10,'\n',sign,'*'*10)
printcross()
dogame()
printcross()
dogame()
printcross()
