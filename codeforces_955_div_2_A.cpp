// codeforces_955_div_2_A.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
 
#include <iostream>
#include <stdio.h>
 
using namespace std;
 
int main()
{
    int t,i,j,k;
    cin >> t;
 
    int x1[t], y1[t], x2[t], y2[t];
 
    for (i = 0; i < t; i++)
    {
        cin >> x1[i] >> y1[i];
        cin >> x2[i] >> y2[i];
    }
    
    for ( i = 0; i < t; i++)
    {
        if (x1[i] > y1[i])
        {
            //x1[i] = x2[i];
            if ( y2[i] < x2[i] )
            {
                printf("YES\n");
            }
            else
            {
                printf("NO\n");
            }
        }
        else if ( y1[i] > x1[i] )
        {
            if ( x2[i] < y2[i])
            {
                printf("YES\n");
            }
            else
            {
                printf("NO\n");
            }
        }
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