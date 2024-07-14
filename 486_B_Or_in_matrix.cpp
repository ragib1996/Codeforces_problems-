// OR_in_matrix.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int m, n;
    cin >> m >> n;
    int a[m][n], matrix[m][n], i, j,k,l;
    for (i = 0; i< m; i++)
    {
        for (j = 0; j<n ; j++)
        {
            matrix[i][j] = -1;
        }
    }
    
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            cin >> a[i][j];
            if (a[i][j] == 0)
            {
                for (k = 0; k < n; k++)
                {
                    matrix[i][k] = 0;
                    //matrix[k][j] = 0;
                }
                for (k = 0; k < m; k++)
                {
                    matrix[k][j] = 0;
                }
            }


        }
    }

    bool flag = false, ismatrix = true;;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (a[i][j] == 1)
            {
                flag = false;
                for (k = 0; k < n; k++)
                {
                    if (matrix[i][k] != 0)
                    {
                        matrix[i][k] = 1;
                        flag = true;
                    }
                }
                for (k = 0; k < m; k++)
                {
                    if (matrix[k][j] != 0)
                    {
                        matrix[k][j] = 1;
                        flag = true;
                    }
                }
            }
            if ( a[i][j] == 1 && flag == false)
            {
                ismatrix = false;
                cout << "NO";
                return 0;
            }
        }
    }

    cout << "YES\n";

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n ; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << "\n";
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
