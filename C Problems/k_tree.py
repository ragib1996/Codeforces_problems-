# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n,k,d = map(int , (input().split()))
    ans = []
    ans.append([1,0])

    for i in range(1, n+1):
        ans.append([0,0])
        for j in range(1, k+1):
            if j <= i:
                if j < d:
                    ans[i][0] += ans[i-j][0]
                    ans[i][1] += ans[i-j][1]
                else:
                    ans[i][1] += ans[i-j][0]
                    ans[i][1] += ans[i-j][1]


    print(ans[n][1] % 1000000007)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
