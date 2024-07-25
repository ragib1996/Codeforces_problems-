// codeforces_Petya_&_staircases.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    int n, m, i,j,k,l;
    cin >> n >> m;

    int a[3000];

    for (i = 0; i < m; i++)
    {
        cin >> a[i];
    }
    sort(a, a + m);
    int current_position = 1;
    bool b = true;

    if (a[0] == 1 || a[m - 1] == n)
    {
        b = false;
    }

    for (i = 0; i < m; i++)
    {
        if (b == false)
        {
            break;
        }
        current_position = a[i] - 1;
        if (current_position + 2 == a[i + 1] ) // && current_position + 3 == a[i+2] )
        {
            if (i + 2 < m)
            {
                if (current_position + 3 == a[i + 2])
                {
                    b = false;
                }
            }
        }
    }

    if (b == true)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
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
