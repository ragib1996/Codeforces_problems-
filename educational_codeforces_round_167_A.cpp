/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

// Problem link : https://codeforces.com/contest/1989/problem/A
#include <iostream>
#include<stdio.h>
using namespace std;


int main()
{
    int i,j,k,n;
    scanf("%d", &n);
    int a[n][2];
    
    for ( i = 0; i < n; i++)
    {
        scanf("%d %d", & a[i][0], & a[i][1]);
    }
    
    for (i = 0; i < n ; i++ )
    {
        if ( a[i][1] >= -1)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}
