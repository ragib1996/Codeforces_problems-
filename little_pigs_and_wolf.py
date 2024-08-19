# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n, m = map(int, input().split())
    row = []
    for i in range(0, n):
        a = input()
        row.append(a)

    ans  = 0
    for i in range(0, n):
        for j in range(0, m):
            if row[i][j] == 'W':
                if i - 1 >= 0 and row[i-1][j] == 'P':
                    ans = ans + 1
                    row[i][j].replace('P', '.')
                elif j+1 < m and row[i][j+1] == 'P':
                    ans = ans + 1
                    row[i][j+1].replace('P', '.')
                elif j-1 >= 0 and row[i][j-1] == 'P':
                    ans = ans + 1
                    row[i][j-1].replace('P', '.')
                elif i+1 < n and row[i+1][j] == 'P':
                    ans = ans + 1
                    row[i+1][j].replace('P', '.')

    print(ans)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
