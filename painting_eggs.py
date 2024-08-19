# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum_a = 0
    sum_g = 0
    n = int(input())
    b =  True
    ans  = ""

    for i in range(0, n):
        a, g = map(int, input().split())

        if a <= g and sum_a + a - sum_g <= 500:
            sum_a = sum_a + a
            ans += 'A'
        elif a <= g and sum_a + a - sum_g > 500:
            sum_g = sum_g + g
            ans += 'G'
        elif g <= a and sum_g + g - sum_a <= 500:
            sum_g = sum_g + g
            ans += 'G'
        elif g <= a and sum_g + g - sum_a > 500:
            sum_a = sum_a + a
            ans += 'A'
        else:
            b = False
            ans = -1
            break

    print(ans)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
