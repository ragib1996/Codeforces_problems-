# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n  = int (input())
    a = list(map(int , input().split()))
    ans = float(0)
    a.sort(reverse= True)

    for i in range (0, len(a)):
        if i%2 == 0:
            ans = ans + math.pi * float(a[i]) * float(a[i])
        else:
            ans = ans - math.pi * float(a[i]) * float(a[i])

    print(ans)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
