# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n, m = map(int, input().split())
    is_center = [True] * (n + 1 )
    for i in range(1, m+1):
        a = list(map(int, input().split()))
        is_center[a[0]] = False
        is_center[a[1]] = False

    c = 0
    for i in range(1, n+1):
        if is_center[i] == True:
            c = i
            break

    print(n-1)
    for i in range(1, n+1):
        if i != c:
            print(i," ", c)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
