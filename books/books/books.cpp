#include <iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    int i, j, k= 0 , n, t, books = 0, times = 0, max_books = 0;
    cin >> n >> t;
    int a[100000];

    for (i = 0; i < n; i++)
    {
        cin >> a[i];
    }
   

    for (i = 0; i < n; i++)
    {
        if (times + a[i] <= t)
        {
            times = times + a[i];
            books++;
        }
        else
        {

            times = times - a[k]+a[i];
            k++; 
        }

        if (books > max_books)
        {
            max_books = books;
        }
    }

    cout << max_books;
}