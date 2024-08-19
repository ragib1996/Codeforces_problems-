# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d, sumtime = map(int , input().split())
    minsum = 0
    maxsum = 0
    ans = []
    tmin = []
    tmax = []
    d0 = 0
    d1 = 0

    for i in range(0, d):
        mintime, maxtime = map(int , input().split())
        ans.append(maxtime)
        tmax.append(maxtime)
        tmin.append(mintime)
        minsum = minsum + mintime
        maxsum = maxsum + maxtime

    if sumtime >= minsum and sumtime <= maxsum:
        print("YES")
        d0 = maxsum - sumtime
        for i  in range(0, d):
            d1 = tmax[i] - tmin[i]
            if d0 == 0:
                print(ans[i], end=' ')
            elif d0 > d1:
                ans[i] = tmin[i]
                print(ans[i], end=' ')
                d0 = d0 - d1
            else:
                ans[i] = ans[i] - d0
                d0 = 0
                print(ans[i], end=' ')


    else:
        print("NO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
