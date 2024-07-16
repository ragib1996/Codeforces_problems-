// little_girl_&_game_276_B.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<stdio.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int n[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}, i, j, k, odd_count = 0;
    for (i = 0; i < s.size(); i++)
    {
        n[s[i] - 'a']++;
    }

    for (i = 0; i < 26; i++)
    {
        if (n[i] % 2 == 1)
        {
            odd_count++;
        }
    }

    if (odd_count == 0 || odd_count % 2 == 1)
    {
        cout << "First";
    }
    else
    {
        cout << "Second";
    }
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
