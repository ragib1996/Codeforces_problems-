#include <stdio.h>
#include<iostream>
#include<vector>

typedef long long int ll;


using namespace std;

int main()
{
    ll n, a,  c, i, j;
    cin >> n;
    vector <int> v1, v2;
    ll v1_sum = 0, v2_sum = 0;
    bool flag = 1;

    for (i = 0; i < n; i++)
    {
        cin >> a;
        if (a > 0)
        {
            v1.push_back(a);
            v1_sum += a;
            flag = 1;
        }
        else
        {
            v2.push_back(a * (-1));
            v2_sum += (a * (-1));
            flag = 0;
        }
    }

    if (v1_sum > v2_sum)
    {
        cout << "first";
    }
    else if (v1_sum < v2_sum)
    {
        cout << "second";
    }
    else if (v1.size() == v2.size() and v1 == v2)
    {
        if (flag == 1)
        {
            cout << "first";
        }
        else
        {
            cout << "second";
        }
    }
    else
    {
        i = 0;
        while (i != v1.size() and i != v2.size())
        {
            if (v1[i] > v2[i])
            {
                cout << "first";
                break;
            }
            else if (v1[i] < v2[i])
            {
                cout << "second";
                break;
            }
            i++;
        }
    }

    return 0;
}