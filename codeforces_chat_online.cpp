// codeforces_chat_online.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<stdio.h>
#include<vector>

using namespace std;

int main()
{
    int p, q, l, r,i,j,k ;
    cin >> p >> q >> l >> r;


    int a[60], b[60], c[60], d[60], t[2002];

    for (i = 0; i < 2002; i++)
    {
        t[i] = 0;
    }

    for (i = 0; i < 60; i++)
    {
        if (i < p)
        {
            cin >> a[i] >> b[i];
            for (j = a[i]; j <= b[i]; j++)
            {
                t[j] = 1;
            }
        }
        else
        {
            a[i] = -1;
            b[i] = -1;
        }
    }

    for (i = 0; i < 60; i++)
    {
        if (i < q)
        {
            cin >> c[i] >> d[i];
        }
        else
        {
            c[i] = -1;
            d[i] = -1;
        }
    }

    int ans = 0;

    
    for (i = l; i <= r; i++)
    {
        for (j = 0; j <  q; j++)
        {
            for (k = i + c[j]; k <= i + d[j]; k++)
            {
                if (t[k] == 1)
                {

                    ans++;
                    //cout << i << " " << ans << "\n";
                    break;
                }
            }
            if (k < i + d[j] + 1)
            {
                break;
            }
        }
    }

    cout << ans;

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
