# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d = {}
    d['>'] = '1000'
    d['<'] = '1001'
    d['+'] = '1010'
    d['-'] = '1011'
    d['.'] = '1100'
    d[','] = '1101'
    d['['] = '1110'
    d[']'] = '1111'

    n = input()
    l = len(n)
    sum = 0
    m = 1
    concatenation = ''

    for i in n:
        concatenation = concatenation + d[i]

    l = len(concatenation)
    for i in range(0, l):
        if i != 0:
            m = m * 2
        sum = sum + m * int(concatenation[l-1-i])

    ans = sum % 1000003
    print(ans)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
