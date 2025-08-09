/*
 * NoxPrime.cpp
 *
 *  Created on: 8.8.2025
 *      Author: Perceus Adalian
 */

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

int main()
{
	bool exitStatus = true;

	while (exitStatus)
	{
		int renderChars;

		std::cout << "Hello. Thank you for choosing to generate your password with NoxPrime." << std::endl;
		std::cout << "Please choose a length for your password: ";
		std::cin >> renderChars;

		if (std::cin.fail())
		{
			std::cin.clear();
			std::cin.ignore(10000);
			std::cout << "Invalid input; was expecting an integer." << std::endl;
			continue;
		}
		else if (renderChars <= 0 || renderChars > 20)
		{
			std::cout << "Invalid input; was expecting 0<=value<=20" << std::endl;
			continue;
		}

		srand(static_cast<unsigned int>(time(0)));
		std::string validCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
		std::string passwordString = "";
		for (int i = 0; i < renderChars; i++)
		{
			int randomIndex = rand() % validCharacters.length();
			passwordString += validCharacters[randomIndex];
		}

		std::cout << "Password Generated with " << renderChars << " characters: " << passwordString << std::endl;
		exitStatus = false;
	}
	return 0;
}
