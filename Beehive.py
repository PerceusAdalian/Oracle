# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:25:15 2024

@author: perceus
"""

def main():
    
    def parseBinary(binary_string):
        '''Returns binary string as it's equivalent integer'''
        return int(binary_string, 2)
    
    def parseHex(binary_string):
        '''Returns binary string as it's hex equivalent'''
        newString = ''
        for i in range(0, len(binary_string), 4):
            segment = binary_string[i:i+4]
            if parseBinary(segment) == 10: 
                newString += 'A'
            elif parseBinary(segment) == 11: 
                newString += 'B'
            elif parseBinary(segment) == 12:
                newString += 'C'
            elif parseBinary(segment) == 13:
                newString += 'D'
            elif parseBinary(segment) == 14:
                newString += 'E'
            elif parseBinary(segment) == 15:
                newString += 'F'
            else:
                newString = newString + str(parseBinary(segment))
        return newString
    
    while True:    
        '''Evaluates the bit-string into both hex and decimal equivalents'''
        response = input("Input Binary String: ")
        if response =="EXIT":
            return False
        hex_value = parseHex(response)
        decimal_value = parseBinary(response)
        print(f"Hex Value: 0x{hex_value} || Decimal Value: {decimal_value}")
main()