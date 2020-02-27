#include "pch.h"
#include <iostream>

using namespace std;

	bool verifystrpalandrome(char* str, int size)
	{
		char* endstr = str + size - 1;
		while (endstr != str)
		{
			if (*str != *endstr)
				return false;
			str++;
			endstr--;
		}
		return true;
	}

int main()
{
	int * p = new int;
	char* name = new char[10];
	strcpy(name, "TeasaeT");
	int size = strlen(name);
	bool b = verifystrpalandrome(name, size);
	if (b == true)
		cout << " palendrome";
	else
		cout << " not palendrome";
}