# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n,m = map(int, input().split())
    ans = ''
    b = True
    if  m > 2*n+2 or  m < n-1:
        ans = str(-1)
        b = False
    elif m == n-1:
        while n >0 and m > 0:
            #print('0', end='')
            ans += '0'
            n-= 1
            #print('1', end='')
            ans += '1'
            m -= 1
        if n != 0 :
            ans += '0'
            #print('0')
    else:
        while m != n and m >0 and n > 0:
            ans += '110'
            #print('110', end='')
            n -= 1
            m -= 2
        while m != 0 and n != 0:
            ans += '10'
            #print('10', end = '')
            m-=1
            n-=1
        while m <= 2 and m >0:
            ans += '1'
            #print('1', end='')
            m -= 1

    print(ans)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
