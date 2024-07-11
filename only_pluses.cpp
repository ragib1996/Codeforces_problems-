/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int i,j,k,b[n][3], a[3], t, ans[3];
    
    
    for (i =0; i<n;i++)
    {
       cin >> b[i][0] >> b[i][1] >> b[i][2];
    }
      
    for (i = 0; i< n; i++)
    {
        
        a[0] = b[i][0], a[1]= b[i][1], a[2] = b[i][2];
        t = 0;
        while (t<5)
        {
            sort (a, a+3);
            if (a[1] == a[0])
            {
                a[0]++;
                t++;
                if (t <5)
                {
                    a[1]++;
                    t++;
                }
            }
            else if (a[1] - a[0] >=5)
            {
                a[0] += 5;
                t = t + 5;
            }
            else if ( a[1] - a[0] < 5)
            {
                t = t + (a[1] - a[0]);
                a[0] = a[0] + ( a[1] - a[0] );
                
            }
        }
        
        cout << a[0] * a[1] * a[2] << "\n";
    
   }
    

    return 0;
}