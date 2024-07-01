#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int n,i,j,k,l, ans = 0;
    scanf("%d", &n);
    
    int a[n][2];
    
    for (i = 0; i<n ; i++)
    {
        cin >> a[i][0] >> a[i][1];
    }
    
    /*
    for (i = 0; i<n ; i++)
    {
        cout  << a[i][0] << " " << a[i][1]<< "\n";
    }
    */
    
    for ( i = 0; i< n; i++)
    {
        ans = 1 + (a[i][0] - 1) * a[i][1];
        cout << ans << "\n";
    }
 
    return 0;
}