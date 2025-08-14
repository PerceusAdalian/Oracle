'''
Author: Perceus Adalian
Date: 8.9.2025 @ 2:23pm
Description: A simple number parser.
'''
import time

stringMap = {2 : "Binary", 10 : "Decimal", 8 : "Octal", 16 : "Hexadecimal"}
digitMap = {ch: i for i, ch in enumerate("0123456789ABCDEF")}
digitsList = "0123456789ABCDEF"

def animatePrint(string, timeSeconds):
    if not string:
        return
    delay = timeSeconds / len(string)
    for ch in string:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def toDecimal(inputStr, base, digitMap):
    inputStr = str(inputStr).upper()
    value = 0
    for ch in inputStr:
        if ch not in digitMap or digitMap[ch] >= base:
            raise ValueError(f'Invalid base: {ch}')  
        value = value * base + digitMap[ch]
    return value

def fromDecimal(value, base, digitsList):
    if value == 0:
        return digitsList[0]
    result = ''
    while value > 0:
        result = digitsList[value % base] + result
        value //= base
    return result

def convert(inputStr, fromBase, toBase):
    decimalValue = toDecimal(inputStr, fromBase, digitMap)
    return fromDecimal(decimalValue, toBase, digitsList)

def isValid(inputStr):
    for char in inputStr:
        if char not in digitMap:
            raise ValueError(f'Invalid input: {char} in {inputStr} is Undefined.')
    return True

def main():
    animatePrint(f'''Beehive Prime: A simple number converter.
    Options: 
    - [1] Convert Binary
    - [2] Convert Integer
    - [3] Convert Hexadecimal
    - [4] Convert Octal
    ''', 2)
    
    while True:
        
        option = input('Please make a selection or type [h]elp/[e]xit: ')
        if option == 'h':
            animatePrint(f'''
    Options: 
    - [1] Convert Binary
    - [2] Convert Integer
    - [3] Convert Hexadecimal
    - [4] Convert Octal
    ''',2)
            continue
        if option == 'e':
            animatePrint(f'Exiting program..',1)
            break
        if option == '1':
            value = input('Enter Binary String: ')
            if isValid(value):
                animatePrint(f'''This Binary ({value}) is: 
- {convert(value, 2, 10)} in Decimal.
- {convert(value, 2, 16)} in Hex.
- {convert(value, 2, 8)} in Octal.''',2)
        elif option == '2':
            value = input('Enter an Integer Value: ')
            if isValid(value):    
                animatePrint(f'''This Integer ({value}) is:
- {convert(value, 10, 2)} in Binary.
- {convert(value, 10, 16)} in Hex.
- {convert(value, 10, 8)} in Octal.''',2)
        elif option == '3':
            value = input('Enter Hexadecimal String: ')
            if isValid(value):
                animatePrint(f'''This Hex ({value}) is:
- {convert(value, 16, 2)} in Binary.
- {convert(value, 16, 10)} in Decimal.
- {convert(value, 16, 8)} in Octal.''',2)
        elif option == '4':
            value = input('Enter an Octal String: ')
            if isValid(value):
                animatePrint(f'''This Octal Value ({value}) is:
- {convert(value, 8, 2)} in Binary.
- {convert(value, 8, 10)} in Decimal.
- {convert(value, 8, 16)} in Hex''',2)
        else:
            animatePrint(f'Unexpected Operand ({option}), please try again.',1)
            continue

        continueGen = input('|$| Continue? [0/y]es | [1/n]o : ')
        if continueGen == 'y' or continueGen == 0:
            continue
        elif continueGen == 'n' or continueGen == 1:
            animatePrint(f'Exiting program..',1)
            break
        break
    
    return 0
main()


