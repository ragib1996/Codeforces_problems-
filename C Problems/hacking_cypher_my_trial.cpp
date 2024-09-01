// hacking_cypher_my_trial.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<stdio.h>

using namespace std;

int main()
{
    string c;
    cin >> c;

    long long int a, b;
    cin >> a >> b;

    long long int prefix[c.size() + 1 ], suffix[c.size() + 1 ], i, j, k;
    
    
    suffix[c.size()] = 0, prefix[c.size()] = 0;
    int p = 1;
    for (i = c.size() - 1; i >= 0; i-- )
    {
        suffix[i] = suffix[i + 1] + (c[i] - '0') * p;
        suffix[i] = suffix[i] % b;
        p = (p * 10) % b;
    }


    for (i = 0; i < c.size(); i++)
    {
        if (i == 0)
        {
            prefix[i] = (c[i] - '0');
        }
        else
        {
            prefix[i] = prefix[i - 1] * 10 + (c[i] - '0'); 
        }
        prefix[i] = prefix[i] % a;
    }


    int ans1 = 0;
    int ans2 = 0;
    bool is_ans = 0;

    for (i = 0; i + 1 < c.size(); i++)
    {
        if (prefix[i] == 0 && suffix[i + 1] == 0 && c[i + 1] != '0')
        {
            is_ans = 1;
            ans1 = i;
            ans2 = i + 1;
        }
    }

    if (is_ans == 0)
    {
        cout << "NO";
    }
    else
    {
        cout << "YES\n";
        cout << c.substr(0, ans2);
        cout << "\n" << c.substr(ans2, c.size() - ans2);
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
