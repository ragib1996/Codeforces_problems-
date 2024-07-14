// suffix_structures.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<stdio.h>
#include<algorithm>
#include <string>

using namespace std;

bool f(string s, string t)
{
	sort(s.begin(), s.end());
	sort(t.begin(), t.end());

	return s == t;
}

bool is_automation(string s, string t)
{
	int i=0,j,k,n = 0;
	
	while (true)
	{
		if (i == s.length() || n == t.length( ) )
		{
			break;
		}

		if (s[i] == t[n])
		{
			n++;
		}
		i++;
	}

	if (n == t.length())
	{
		return true;
	}
	return false;
}

bool is_both(string s, string t)
{
	int i, j, k, b = -5;

	for (i = 0; i < t.length(); i++ )
	{
		b = s.find(t[i]);
		
		if (b == -1)
		{
			return false;
		}
		s[b] = '0';
	}

	return true;
}

int main()
{
	string s, t;
	cin >> s;
	cin >> t;
	bool b = f(s, t);
	if (b == 1)
	{
		cout << "array";
		return 0;
	}
	b = is_automation(s, t);
	if (b == 1)
	{
		cout << "automaton";
		return 0;
	}
	b = is_both(s, t);
	if (b == 1)
	{
		cout << "both";
		return 0;
	}
	else
	{
		cout << "need tree";
	}
	
	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
