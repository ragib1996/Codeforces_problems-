# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    left = [0] * 100001
    right = [0] * 100001
    n= int (input())
    a = []
    for i in range(0, n):
        x,y = map (int, (input().split()))
        left[x] += 1
        right[y] += 1
        a.append([x,y])
    #print(n)
    #for i in range(0,n):
    #    print(a[i][0]," ",a[i][1])
    ans = []
    for i in range(0, n):
        x = n-1
        x += left[a[i][1]]
        match = 2 * (n-1)
        y = match - x
        ans.append([x,y])

    for i in range(0, n):
        print(ans[i][0]," ", ans[i][1])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
