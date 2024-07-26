# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t = int (input())
    n = []
    k = []
    user_input = []
    for i in range(0, t):

        x, y = map(int, input().split())
        n.append(x)
        k.append(y)
        s2 = []
        for j in range(0,x):
            s = input()
            s2.append(s)
        user_input.append(s2)

    ans = []
    for i in range(0,t):
        sample = user_input[i]
        a = []
        for x in range(0, len(sample), k[i] ):
            s = ""
            for y in range (0, len(sample), k[i] ):
                s+=sample[x][y]
            a.append(s)

        for z1 in range(0, len(a)):
            print(a[z1])
















# See PyCharm help at https://www.jetbrains.com/help/pycharm/
