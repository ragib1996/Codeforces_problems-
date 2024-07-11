/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include<bits/stdc++.h>

using namespace std;



int main()
{
    int t, i,j, x, y, z, operations = 0;
    cin >> t;
    
    int n[t], k[t];
    std::vector<int> ans  ;
    
    for (i = 0; i< t; i++)
    {
        cin >> n[i] >> k[i];
        int a[k[i]];
        for (j = 0; j< k[i]; j++)
        {
            cin >> a[j];
        }
        
        sort (a, a + k[i]);
        operations = 0;
        for (x=0; x < k[i] - 1 ;x++ )
        {
            operations = operations + (a[x]-1) + a[x];
        }
        ans.insert( ans.begin() + i, operations);
    }
    
    for (i = 0; i< ans.size(); i++)
    {
        cout << ans[i] << "\n";
    }
    return 0;
}