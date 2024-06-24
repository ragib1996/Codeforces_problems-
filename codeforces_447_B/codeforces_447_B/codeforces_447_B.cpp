// Source : https://github.com/w181496/OJ/blob/master/CodeForces/447B%20-%20DZY%20Loves%20Strings.cpp

#include<iostream>
#include<string>
#include<algorithm>
#include <stdio.h>
using namespace std;
int main()
{
    string s;
    int i, j, k, l;
    int ans = 0;

    int w[26];

    cin >> s;
    cin >> k;
    for (i = 0; i < 26; i++)
    {
        cin >> w[i];
    }

    for (i = 0; i < s.size(); i++)
    {
        ans = ans + w[(s[i] - 'a')] * (i + 1);
    }
    l = w[0];
    for (i = 0; i < 26; i++)
    {
        if (w[i] > l)
        {
            l = w[i];
        }
    }

    for (i = 0; i < k; i++)
    {
        ans = ans + l * (s.size() + i + 1 );
    }

    printf("%d", ans);
    return 0;
}