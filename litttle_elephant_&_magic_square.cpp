// litttle_elephant_&_magic_square.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int a[3][3], i, j, k, c0 , c1, c2;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            cin >> a[i][j];
        }
    }

    c0 = a[0][0] + a[0][1] + a[0][2];
    c1 = a[1][0] + a[1][1] + a[1][2];
    c2 = a[2][0] + a[2][1] + a[2][2];

    int t = (c0 + c1 + c2) / 2;

    a[0][0] = t - c0;
    a[1][1] = t - c1;
    a[2][2] = t - c2;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << "\n";
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
