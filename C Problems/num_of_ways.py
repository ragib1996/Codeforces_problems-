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

    sum  = 0
    ans = 0
    for i in a:
        sum += i

    b = True
    one_third = sum/3
    num_one_third = 0
    two_third = 2 * one_third
    num_two_third = 0
    if sum % 3 != 0:
        b = False

    s = 0
    for i in range(0,len(a) - 1):
        if b == False:
            break
        s = s + a[i]
        if s == two_third:
            if num_one_third >= 1:
               ans += num_one_third
        if s == one_third:
            num_one_third += 1


    print(ans)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
