import math

def factorial(n):
    if n < 0:
        raise ValueError('Undefined input: Negative integer')
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    
    while True:
        var = int(input('Enter any positive number: '))
        print(f'The factorial of {var} is {factorial(var)}')
        
        continueGen = input('|$| Continue? [0/y]es | [1/n]o : ')
        if continueGen == 'y' or continueGen == 0:
            continue
        elif continueGen == 'n' or continueGen == 1:
            break
        break
    return 0
main()