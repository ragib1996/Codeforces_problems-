# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n,m = map(int, (input().split()))
    check = []
    if n == m:
        print(n+1)
        for i in range(0,n):
            print(i," ",n-i)

        print(n," ",0)
    elif n < m:
       print(n+1)
       for i in range(0, n+1):
           print(i, " ", i+1)
    else:
        print(m+1)
        for i in range(0, m+1):
            print(i+1," ",i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
