# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int (input())
    d = {}

    for i in range(0,n):
        a, b = map(int , input().split())
        if b not in d:
            d[b] = []
        d[b].append(a)

    points = 0
    c = 1

    for i in sorted(d, reverse= True):
        l = d[i]
        l.sort(reverse= True)
        for j in l:
            if c == 0:
                break
            points =  points +j
            c = c - 1
            c = c + i

    print(points)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
