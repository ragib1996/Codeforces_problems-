# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int (input())
    a = list(map(int, input().split()))
    not_acceptable = 0
    d = {}

    for i in range(0, len(a), 1):
        if a[i] not in d:
            d[a[i] ] = []
        if len(d[a[i]]) < 2 or d[a[i]][-1] != -1:
            d[a[i]].append(i)
        if len(d[a[i]]) >=3:
            if d[a[i]][-1] != -1:
                if d[a[i]][-1] - d[a[i]][-2] != d[a[i]][-2] - d[a[i]][-3]:
                    d[a[i]].pop()
                    d[a[i]].append(-1)
                    not_acceptable += 1

    print(len(d) - not_acceptable)
    for i in sorted(d):
        if len(d[i]) == 1:
            print(i," ",0)
        elif d[i][-1] != -1:
            print(i," ", d[i][-1]- d[i][-2])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
