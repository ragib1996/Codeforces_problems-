# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n, m = map (int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    i = n-1
    j = m-1
    c = 0

    while i >= 0 and j >= 0 :
        if b[j] >= a[i]:
            c += 1
            j = j - 1
        i = i - 1

    print(n - c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
