import random
import string
import time

def animatePrint(string, timeSeconds):
    if not string:
        return
    delay = timeSeconds / len(string)
    for ch in string:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    animatePrint('ν/NOX: Password Generator', 1.25)
    
    while True:
        
        try:
            renderChars = int(input('Enter a value to generate a password: '))
        except ValueError:
            print('Invalid input; was expecting an integer.')
            continue
        if renderChars <= 0 or renderChars > 100:
            print('Invalid input; was expecting 0 < VALUE <= 100')
            continue
    
        validCharacters = string.ascii_letters + string.digits + f'!@#$%^&*()'
        passwordString = ''
    
        for i in range(renderChars):
            randomIndex = random.randint(0, len(validCharacters) - 1)
            index = randomIndex+0
            passwordString += validCharacters[index]

        animatePrint(f'Generating Password w/ {renderChars} Characters:',1.25)
        animatePrint(passwordString,2)
        
        continueGen = input('|$| Continue? [0/y]es | [1/n]o : ')
        if continueGen == 'y' or continueGen == 0:
            continue
        elif continueGen == 'n' or continueGen == 1:
            break
        break
    return 0                
           
main()