// find_marble.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int n, s, t, i,j,k;
    cin >> n >> s >> t;
    int a[n+1];
    a[0] = 0;

    for (i = 1; i < n+1 ; i++)
    {
        cin >> a[i];
    }

    int current_position = s, next_position = -1, step = 0;

    while (current_position != t )
    {
        next_position = a[current_position];
        a[current_position] = -1;
        if (next_position == -1)
        {
            cout << next_position;
            return 0;
        }
        current_position = next_position;
        step++;
    }
    
    cout << step;

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
