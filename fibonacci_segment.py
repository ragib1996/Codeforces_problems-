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
    current_len = 0
    max_len = 0
    if n > 2:

       i = 2
       max_len = 2
       current_len = 2
       is_fib = True
    else:
        max_len = n

    i = 0
    for i in range(2, len(a)):
        is_fib = True
        if a[i] == a[i-1] + a[i-2]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            is_fib = False
            current_len = 2

    if i+1 == len(a) and current_len > max_len:
        max_len = current_len

    print(max_len)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
