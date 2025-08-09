#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int parseBinary(const string& binaryString)
{
    int decimalValue = 0;
    for (char bit : binaryString)
    {
        if (bit != '0' && bit != '1') return -1; // Invalid binary input
        decimalValue = (decimalValue << 1) | (bit - '0'); // Bitwise shift approach
    }
    return decimalValue;
}

string parseHex(const string& binaryString)
{
    string parsedString;
    int len = binaryString.length();

    // Ensure length is a multiple of 4 (pad if needed)
    int padLength = (4 - (len % 4)) % 4;
    string paddedBinary = string(padLength, '0') + binaryString;

    for (size_t i = 0; i < paddedBinary.length(); i += 4)
    {
        string segment = paddedBinary.substr(i, 4);
        int decimalValue = stoi(segment, nullptr, 2); // Convert binary to decimal

        char letter;
        if (decimalValue < 10)
            letter = '0' + decimalValue; // '0'-'9'
        else
            letter = 'A' + (decimalValue - 10); // 'A'-'F'

        parsedString += letter;
    }
    return parsedString;
}

int main()
{
    string binaryString;
    cout << "Enter a binary string: ";
    cin >> binaryString;

    cout << "Binary as Decimal: " << parseBinary(binaryString) << endl;
    cout << "Binary as Hex: " << parseHex(binaryString) << endl;

    return 0;
}