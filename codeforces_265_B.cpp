/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    
    
    int n;
    scanf("%d", &n);
    int a[n];
    int i,j,k,l, t = 0;
    for (i = 0; i< n; i++ )
    {
        scanf("%d", &a[i]);
    }
    
    for ( i = 0; i<n; i++)
    {
       if ( i == 0)
       {
           t = t + a[i] + 1;
       }
       else
       {
           if (a[i] > a[i-1] )
           {
               t = t+ 1 + (a[i] - a[i-1] ) + 1; // first climb to next tree , go to top and eat nut
           }
           else
           {
               t = t+ (a[i-1] - a[i] ) + 1 + 1;  // first climb down , jump and eat 
           }
       }
    }
    
    printf("%d", t);
    return 0;
}