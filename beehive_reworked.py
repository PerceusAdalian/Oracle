def parseBinary(binary_string):
    """Returns binary string as its equivalent integer."""
    return int(binary_string, 2)

def parseHex(binary_string):
    """Returns binary string as its hex equivalent."""
    newString = ''
    for i in range(0, len(binary_string), 4):
        segment = binary_string[i:i+4]
        decimal_value = parseBinary(segment)  # Compute once
        
        if decimal_value >= 10:
            newString += chr(55 + decimal_value)  # Convert 10-15 to A-F
        else:
            newString += str(decimal_value)
    
    return newString

def main():
    """Evaluates the bit-string into both hex and decimal equivalents."""
    while True:
        response = input("Input Binary String: ").strip()
        if response.upper() == "EXIT":
            break
        
        hex_value = parseHex(response)
        decimal_value = parseBinary(response)
        print(f"Hex Value: 0x{hex_value} || Decimal Value: {decimal_value}")

main()