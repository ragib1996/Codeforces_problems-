# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x, y = map (int, (input().split()))
    #print(x," ", y)
    n = int (input())
    #print(n)

    f = [x, y, y-x, -x, -y, -y+x]
    k = n % 6
    if k == 0:
        ans = f[5]
    else:
        ans = f[k-1]

    print(ans % 1000000007)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
